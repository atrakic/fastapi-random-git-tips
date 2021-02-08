import os
import json
import random

from fastapi import FastAPI

from app.api import ping

jf = os.getenv('JSON_FILE', 'git-tips.json')

app = FastAPI()
app.include_router(ping.router)

@app.get("/")
async def random_tip():
    with open(jf) as json_file:
        d = json.load(json_file)
        return random.sample(d, 1)
