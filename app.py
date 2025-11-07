from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model='gpt2')

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_text = ''
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        result = generator(prompt, max_length=100)
        generated_text = result[0]['generated_text']
    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
