from langchain_openai import ChatOpenAI

from app.config import config
from app.llm.observability import langfuse_handler

gpt_4o_mini = ChatOpenAI(
    model=config.OPENAI_GPT_4O_MINI_MODEL,
    api_key=config.OPENAI_API_KEY,
    callbacks=[langfuse_handler]
)