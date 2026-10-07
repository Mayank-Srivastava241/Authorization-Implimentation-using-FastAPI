# Supabase Auth API

## Overview

FastAPI authentication API using Supabase Auth.

## Features

- User signup
- User login
- JWT authentication
- Protected routes
- Logout
- Swagger documentation

## Setup

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Create .env
5. Start FastAPI server

## Environment Variables

SUPABASE_URL=...
SUPABASE_KEY=...

## Run

uvicorn main:api --reload

## API Endpoints

| Method | Endpoint | Authentication |
|--------|----------|----------------|
| GET | /public | No |
| POST | /auth/signup | No |
| POST | /auth/login | No |
| POST | /auth/logout | Yes |
| GET | /protected/profile | Yes |
| GET | /protected/dashboard | Yes |

## Swagger

http://localhost:8000/docs
