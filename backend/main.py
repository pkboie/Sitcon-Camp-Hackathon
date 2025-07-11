from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os

import google.generativeai as genai

# 讀取你的 Gemini API Key
genai.configure(api_key="AIzaSyBn3NK0lqKeVmNiWd3rWhfqRz2iNfs23i8")

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 部署時改成你的網域
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.get("/")
async def root():
    return FileResponse("../frontend/index.html")


# 👗 AI 穿搭顧問
@app.post("/ask_style")
async def ask_style(prompt: str = Form(...)):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return JSONResponse({"answer": response.text})
