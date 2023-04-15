from typing import List
from .utils import find_cities_in_text,find_aqi_in_text, merge_lists
from langchain.output_parsers import StructuredOutputParser, ResponseSchema



def get_response_schemas() -> List[ResponseSchema]:
    """
    Returns a list of response schemas for the OpenAI API.
    """
    return [
        ResponseSchema(name="answer", description="answer to the user's question"),
        ResponseSchema(name="source", description="source used to answer the user's question, should be a website.")
    ]


class AirQualityOutputParser:
    """
    Parser for the output of the OpenAI air quality API.
    """

    def __init__(self):
        self.response_schemas = get_response_schemas()
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schemas)
        self.format_instructions = self.output_parser.get_format_instructions()

    def parse_output(self, output: str) -> dict:
        response = self.output_parser.parse(output)
        cities = find_cities_in_text(response["answer"])
        aqis = find_aqi_in_text(response["answer"])
        response['data'] = merge_lists(cities, aqis)
        return response
