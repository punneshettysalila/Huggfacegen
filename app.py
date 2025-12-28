import os
from flask import Flask, request, send_file, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model='distilgpt2')

@app.route('/', methods=['GET'])
def home():
    return send_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.form.get('prompt')
        if prompt:
            result = generator(prompt, max_length=100, num_return_sequences=1)
            generated_text = result[0]['generated_text']
            return jsonify({'text': generated_text})
        return jsonify({'text': '', 'error': 'No prompt provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
