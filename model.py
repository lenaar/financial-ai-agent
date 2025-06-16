import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(api_key=openai_api_key, model="gpt-4.1-nano", temperature=0.0)


def generate_model_response(content: str, prompt: str) -> str:
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=content)
    ]

    data = model.invoke(messages)

    return data.content