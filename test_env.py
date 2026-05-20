from dotenv import load_dotenv
import os

loaded = load_dotenv()

print("dotenv loaded:", loaded)

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("Loaded:", True)
    print(api_key[:10] + "...")
else:
    print("No API key found")