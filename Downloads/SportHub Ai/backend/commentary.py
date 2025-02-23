import openai
from match_data import get_live_match_data

# GPT API Key (Replace with actual API key)
OPENAI_API_KEY = "your_openai_api_key"

def generate_commentary(match):
    prompt = f"Provide an enthusiastic commentary for {match['teams'][0]} vs {match['teams'][1]} with a score of {match['score']}."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a sports commentator."},
                  {"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]
