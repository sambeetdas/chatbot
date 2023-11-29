import openai
from dotenv import load_dotenv

os = load_dotenv()
class Api:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPEN_API_SECRECT_KEY")

    def generate_response(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can try other engines as well
            prompt=prompt,
            max_tokens=150,  # Adjust as needed
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()
