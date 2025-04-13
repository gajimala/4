from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware  # CORS 미들웨어 임포트
from typing import Optional
import json
import os

# FastAPI 앱 생성
app = FastAPI(title="Gangneung Lifesaver API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 요청을 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# 데이터 로딩 (파일 경로 및 데이터 읽기)
DATA_PATH = os.path.join(os.path.dirname(__file__), "gangneung_filtered_by_lat.json")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

# 루트 엔드포인트 (문서화 메시지)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Gangneung Lifesaver API. Visit /docs for API documentation."}

# /lifesavers 엔드포인트 (필터링 및 데이터 반환)
@app.get("/lifesavers")
def get_lifesavers(
    address: Optional[str] = Query(None, description="주소에 포함된 텍스트 검색"),
    desc: Optional[str] = Query(None, description="설치장소 설명 검색"),
    pol_nm: Optional[str] = Query(None, description="관할 파출소명 검색")
):
    results = lifesavers  # 전체 데이터
    if address:
        results = [item for item in results if address in str(item.get("address", ""))]
    if desc:
        results = [item for item in results if desc in str(item.get("desc", ""))]
    if pol_nm:
        results = [item for item in results if pol_nm in str(item.get("pol_nm", ""))]
    return results
