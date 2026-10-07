import os
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi import HTTPException, status
from pydantic import BaseModel

load_dotenv()

s_url = os.getenv("SUPABASE_URL")
s_key = os.getenv("SUPABASE_KEY")

supabase = create_client(s_url, s_key)

api = FastAPI()
security = HTTPBearer()

class details(BaseModel):
    email: str
    password: str