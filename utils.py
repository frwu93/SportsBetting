from dotenv import load_dotenv
import os

def get_api_key(name):
    load_dotenv()
    return os.getenv(name)


