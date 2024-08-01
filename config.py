import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LANGFUSE_PUBLIC_KEY = os.getenv('LANGFUSE_PUBLIC_KEY')
    LANGFUSE_SECRET_KEY = os.getenv('LANGFUSE_SECRET_KEY')
    LANGFUSE_HOST = os.getenv('LANGFUSE_HOST', 'https://cloud.langfuse.com')