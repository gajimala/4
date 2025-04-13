from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware  # CORS 미들웨어 임포트
from fastapi.responses import FileResponse  # FileResponse 임포트 추가
from typing import Optional
import json
import os

# FastAPI 앱 생성
app = FastAPI(title="Gangneung Lifesaver API")

# CORS 설정 (모든 도메인에서 요청을 허용)
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
    
    # 필터링 조건
    if address:
        results = [item for item in results if address.lower() in str(item.get("address", "")).lower()]
    if desc:
        results = [item for item in results if desc.lower() in str(item.get("desc", "")).lower()]
    if pol_nm:
        results = [item for item in results if pol_nm.lower() in str(item.get("pol_nm", "")).lower()]

    # 결과가 없을 때 메시지 반환
    if not results:
        return {"message": "No results found matching the search criteria."}
    
    return results

# /static 엔드포인트 (HTML 파일 제공)
@app.get("/static/lifesaver-map.html")
async def get_html():
    file_path = "static/lifesaver-map.html"
    
    # HTML 파일이 존재하면 반환
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "HTML file not found"}
