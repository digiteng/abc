import os
import base64
import requests
from fastapi import FastAPI, HTTPException, Security, status, Response
from fastapi.security.api_key import APIKeyHeader
from mangum import Mangum

app = FastAPI()

TOKEN = os.getenv("TOKEN", "").strip()
URL = os.getenv("URL", "").strip()
API_KEY = os.getenv("MAC_0", "").strip()

API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(header_value: str = Security(api_key_header)):
	if not API_KEY or header_value != API_KEY:
		raise HTTPException(status_code=401, detail="Unauthorized")
	return header_value

@app.get("/run-script")
def run_github_script():
	headers = {
		'accept': 'application/vnd.github.v3.raw',
		'authorization': f'token {TOKEN}',
		'X-GitHub-Api-Version': '2022-11-28',
		'user-agent': 'Vercel-App'
	}
	
	try:
		req = requests.get(URL, headers=headers, timeout=15)
		
		if req.status_code != 200:
			return Response(content=f"# API Hatasi: {req.status_code}", media_type="text/plain")

		return Response(content=script_content.strip(), media_type="text/plain; charset=utf-8")

	except Exception as e:
		return Response(content=f"# Sunucu Hatasi: {str(e)}", media_type="text/plain")

handler = Mangum(app)
