import os
import dotenv

# Load environment variables
dotenv.load_dotenv(dotenv_path=".env")
PORT = os.getenv("PORT") or 8000
CLIENT_DOMAINS = os.getenv("CLIENT_DOMAINS").split(",") or "*"
MODEL_PATH = os.getenv("MODEL_PATH") or ""
