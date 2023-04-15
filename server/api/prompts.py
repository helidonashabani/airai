from langchain.prompts import PromptTemplate
from langchain import PromptTemplate


class AirQualityPrompt:
    """
    Prompt for the OpenAI air quality API.
    """

    def __init__(self, format_instructions: str):
        self.format_instructions = format_instructions


    def create_prompt(self, question: str) -> PromptTemplate:
        prompt_template = self.get_prompt_template()
        return prompt_template.format_prompt(question=question)


    def get_prompt_template(self) -> PromptTemplate:
        """
        Returns a PromptTemplate instance for the OpenAI API.
        """
        return PromptTemplate(
            template="answer the users question as best as possible.\n{format_instructions}\n{question}",
            input_variables=["question"],
            partial_variables={"format_instructions": self.format_instructions}
        )