from fastapi import FastAPI, Query
from typing import List, Optional
import json
import os

app = FastAPI(title="Gangneung Lifesaver API")

# 데이터 로딩
DATA_PATH = os.path.join(os.path.dirname(__file__), "gangneung_filtered_by_lat.json")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/")
def read_root():
return {"message": "Welcome to the Gangneung Lifesaver API. Visit /docs for API documentation."}

@app.get("/lifesavers")
def get_lifesavers(
    address: Optional[str] = Query(None, description="주소에 포함된 텍스트 검색"),
    desc: Optional[str] = Query(None, description="설치장소 설명 검색"),
    pol_nm: Optional[str] = Query(None, description="관할 파출소명 검색")
):
    results = lifesavers
    if address:
        results = [item for item in results if address in str(item.get("address", ""))]
    if desc:
        results = [item for item in results if desc in str(item.get("desc", ""))]
    if pol_nm:
        results = [item for item in results if pol_nm in str(item.get("pol_nm", ""))]
    return results
