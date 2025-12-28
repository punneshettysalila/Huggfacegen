import os
from flask import Flask, request, send_file
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model='gpt2')

@app.route('/', methods=['GET'])
def home():
    return send_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    if prompt:
        result = generator(prompt, max_length=100)
        generated_text = result[0]['generated_text']
        return generated_text
    return ''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
