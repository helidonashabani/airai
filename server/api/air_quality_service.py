from .llms import AirQualityOpenAI
from .output_parser import AirQualityOutputParser
from .prompts import AirQualityPrompt
from .utils import find_cities_in_text,find_aqi_in_text, merge_lists


class AirQualityService:
    def __init__(self, openai: AirQualityOpenAI, parser: AirQualityOutputParser, prompt: AirQualityPrompt):
        self.openai = openai
        self.parser = parser
        self.prompt = prompt

    def get_air_quality(self, prompt: str):
        _input_text = self.prompt.create_prompt(question=prompt)
        output = self.openai.get_response(_input_text.to_string())
        response = self.parser.parse_output(output)
        cities = find_cities_in_text(response["answer"])
        aqis = find_aqi_in_text(response["answer"])
        response['data'] = merge_lists(cities, aqis)
        return response