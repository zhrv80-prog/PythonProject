import requests
from json.decoder import JSONDecodeError

response = requests.get("https://playground.learnqa.ru/api/get_text")

try:
    parsed_response_text = response.json()
    print(response.text)
except JSONDecodeError:
    print("No JSON object could be decoded")

