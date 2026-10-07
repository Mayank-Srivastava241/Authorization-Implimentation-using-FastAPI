import os
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi import FastAPI,Depends
from fastapi.security import HTTPBearer
from fastapi import HTTPException, status
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

s_url = os.getenv("SUPABASE_URL")
s_key = os.getenv("SUPABASE_KEY")

supabase = create_client(s_url, s_key)

api = FastAPI()
security = HTTPBearer()

class details(BaseModel):
    email: str
    password: str

@api.get("/public")
def greet():
    return {
        "message": "Hello Public"
    }

def cur_user(
    creds: HTTPAuthorizationCredentials = Depends(security)
):
    token = creds.credentials

    try:
        response = supabase.auth.get_user(token)
        return response.user

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

@api.get("/protected/profile")
def profile(user=Depends(cur_user)):
    return {
        "token": user.email
    }