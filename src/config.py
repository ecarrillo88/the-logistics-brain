import os

from dotenv import load_dotenv

load_dotenv()

class Config:
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
  OPENAI_GPT_4O_MINI_MODEL = "gpt-4o-mini"

config = Config()