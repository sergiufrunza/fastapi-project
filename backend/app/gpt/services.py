import json
import asyncio
import fitz
import openai
from app.config import settings
import re


async def get_quiz(file_url: str):
    return await asyncio.to_thread(extract_text_from_pdf, file_url)


client = openai.OpenAI(api_key=settings.gpt.api_key)


def extract_text_from_pdf(file_url: str):
    with fitz.open(file_url) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text("text") + "\n"
        prompt = """
Generate a **5 multiple-choice question** based on the following text:
"%s"
The question and answers **must be in the same language** as the provided text.
The response should be in **strict JSON format**, without explanations or additional text. The structure must be exactly as follows:
[
{
    "q": "<Question?>",
    "a": [
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>}
    ]
},
{
    "q": "<Question?>",
    "a": [
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>}
    ]
},
{
    "q": "<Question?>",
    "a": [
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>}
    ]
},
{
    "q": "<Question?>",
    "a": [
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>}
    ]
},
{
    "q": "<Question?>",
    "a": [
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>},
        {"v": "<Answer Option>", "s": <true or false>}
    ]
}

]
Rules:
- All questions must have **exactly 3 answer options**.
- **Only one answer** should be correct (`s: true`), while the other two should be incorrect (`s: false`).
- Do **not** include any additional text, explanations, or JSON labels—only return the final JSON structure.
""" % (
            text,
        )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=3000,
        )

        content = response.choices[0].message.content
        match = re.search(r"\[.*\]", content, re.DOTALL)
        return json.loads(match.group(0))
