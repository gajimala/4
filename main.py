from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 필요 시 특정 도메인으로 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# lifesaver 데이터 불러오기
with open("gangneung_lifesavers.json", encoding="utf-8") as f:
    lifesaver_data = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesaver_data

# 정적 파일 서빙 (여기 중요!)
app.mount("/static", StaticFiles(directory="static"), name="static")
