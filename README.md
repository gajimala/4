
# Gangneung Lifesaver API

## 실행 방법

1. Python 3.7+이 설치되어 있어야 합니다.
2. 터미널에서 다음을 실행하세요:

```
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

3. 브라우저에서 http://127.0.0.1:8000/lifesavers/gangneung 로 접속하면 됩니다.
