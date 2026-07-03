"""
Thin wrapper around the Groq chat completions API.

Keeps the Groq SDK usage in one place so routes/chat.py doesn't need to
know API details, and so it's easy to swap models or providers later.
"""

from groq import Groq

MODEL = "llama-3.1-8b-instant"


class LLMClient:
    def __init__(self, api_key: str):
        self._client = Groq(api_key=api_key)

    def get_completion(self, system_prompt: str, user_message: str) -> str:
        """Send a single-turn completion request and return the reply text."""
        response = self._client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content
