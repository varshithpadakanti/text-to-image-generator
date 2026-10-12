import random
from urllib.parse import quote
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API = "https://image.pollinations.ai/prompt/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return jsonify(error="Please enter a prompt"), 400
    if len(prompt) > 300:
        return jsonify(error="Prompt too long (max 300 chars)"), 400

    size = 512
    seed = random.randint(1, 10**6)
    url = f"{API}{quote(prompt)}?width={size}&height={size}&seed={seed}&nologo=true"
    return jsonify(url=url, seed=seed)

if __name__ == "__main__":
    app.run(debug=True)
