import os
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Global variable for lazy loading
generator = None

def load_model():
    global generator
    if generator is None:
        generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "message": "Text Generation API",
        "endpoints": {
            "/": "GET - API Status",
            "/generate": "POST - Generate text"
        }
    })

@app.route("/generate", methods=["POST"])
def generate():
    try:
        load_model()  # Lazy load model

        data = request.get_json(silent=True) or {}
        prompt = data.get("prompt") or request.form.get("prompt")

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        result = generator(
            prompt,
            max_length=100,
            num_return_sequences=1
        )

        return jsonify({
            "text": result[0]["generated_text"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
