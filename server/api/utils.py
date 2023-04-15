import locationtagger
import nltk
import re
from typing import List, Dict


# essential entity models downloads
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')


def find_cities_in_text(text: str) -> list:
    """
    Extracts the cities mentioned in a text using locationtagger.
    """
    place_entity = locationtagger.find_locations(text=text)
    return place_entity.cities


def find_aqi_in_text(text)-> list:
    # Regular expression patterns
    number_pattern = r"(?:air quality index of |AQI(?: of|:| is| is ))(\d+)"
    category_pattern = r"'(\w(?:\w|\s)*)'"

    # Find all numeric AQI values in the text
    aqi_values = [int(value) for value in re.findall(number_pattern, text)]

    if not aqi_values:
        # Find all air quality categories in the text
        categories = re.findall(category_pattern, text)

        # Mapping of categories to AQI ranges
        category_ranges = {
            'Good': '0-50',
            'Moderate': '51-100',
            'Unhealthy for Sensitive Groups': '101-150',
            'Unhealthy': '151-200',
            'Very Unhealthy': '201-300',
            'Hazardous': '301+',
        }

         # Map categories to AQI ranges
        aqi_values.extend([category_ranges[category] for category in categories])

    return aqi_values


def merge_lists(list_one: List[str], list_two: List[int]) -> Dict[str, int]:
    result = {one: two for one, two in zip(list_one, list_two)}
    return result


def validate_input(data):
    """
    Validates the input data for the air_quality API endpoint.
    """
    if not data:
        return False, "Request data is missing"
    if "question" not in data:
        return False, "The 'question' field is required"
    return True, ""
