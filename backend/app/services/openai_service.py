import openai
from ..config import settings

openai.api_key = settings.openai_api_key

def generate_text(prompt: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
