from langchain_openai import ChatOpenAI
from config import config

llm = ChatOpenAI(
    model=config.OPENAI_MODEL,
    api_key=config.OPENAI_API_KEY,
    temperature=0.2
)

def logistic_operator_response(state):
    return {"response": "The 'Logistic Operator' agent processed the request"}