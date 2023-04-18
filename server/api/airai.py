import logging
from flask import Blueprint, request, jsonify, make_response
from flask_cors import CORS

from .utils import validate_input
from .air_quality_service import AirQualityService
from .llms import AirQualityOpenAI
from .output_parser import AirQualityOutputParser
from .prompts import AirQualityPrompt


API_BLUEPRINT = Blueprint('airai', __name__)
CORS(API_BLUEPRINT)

# set up logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# create instances of the required classes
openai = AirQualityOpenAI()
output_parser = AirQualityOutputParser()
prompt = AirQualityPrompt(output_parser.format_instructions)

@API_BLUEPRINT.route("/air_quality", methods=["POST"])
def air_quality():
    try:
        data = request.get_json()
        is_valid, error_message = validate_input(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        prompt_text = data.get("question", "")
        
        # call the AirQualityService to get the response
        service = AirQualityService(openai, output_parser, prompt)
        response = service.get_air_quality(prompt_text)

        # added Referrer-Policy header to the response
        headers = {'Referrer-Policy': 'no-referrer'}
        return make_response(jsonify(response), 200, headers)

    except Exception as e:
        # log the error
        logger.error(f"Error occurred: {str(e)}")
        # return an error message
        return jsonify({"error": "An error occurred. Please try again later."}), 500

