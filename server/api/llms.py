from langchain.llms import OpenAI


class AirQualityOpenAI:
    """
    OpenAI class for the air quality API.
    """

    def __init__(self, temperature: int = 0):
        self.openai = OpenAI(temperature=temperature)

    def get_response(self, prompt: str) -> str:
        return self.openai(prompt)
