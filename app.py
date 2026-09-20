from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"app": "devops-app", "status": "ok", "version": "1.0.0"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}
