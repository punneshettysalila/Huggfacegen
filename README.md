***

# Text Generation Demo with GPT-2 (HuggingFace & Flask)

This project is a minimal and interactive web app that uses HuggingFace's Transformers library to generate coherent texts from user prompts in real time, powered by a GPT-2 model. It’s designed as a self-driven learning project to explore practical GenAI integration and deployment.

***

## 🌊 Overview

- **Purpose:** To explore and showcase how easy it is to build a GenAI-powered web application using HuggingFace Transformers, Python (Flask), and simple web technologies.
- **What it does:** Users enter any prompt in the web UI and receive a continuation generated live by GPT-2, demonstrating the capabilities of large language models (LLMs) in natural language processing.

***

##  Features

- **Live Text Generation:** Enter any prompt, receive extended AI-generated text instantly.
- **Seamless UI:** Simple HTML/CSS design with floating, animated ocean-inspired background.
- **Backend Integration:** Uses Flask on Python to connect the web UI and HuggingFace model.
- **Self-paced Learning:** All code is commented and modular, encouraging experimentation and study.
- **Extendable:** Swap models, modify prompt handling, or host as an interactive notebook!

***

##  Tech Stack

- **Frontend:** HTML5, CSS3 (animated gradient, sea green & blue color palette)
- **Backend:** Python (Flask)
- **GenAI:** HuggingFace Transformers Library (GPT-2)
- **Other:** Works locally, can be easily extended for deployment or further study.

***

##  Installation & Usage

1. **Clone the Repo**
   ```bash
   git clone https://github.com/yourusername/text-generation-gpt2-demo.git
   cd text-generation-gpt2-demo
   ```

2. **Install Dependencies**
   ```bash
   pip install flask transformers
   ```

3. **Run the App**
   ```bash
   python app.py
   ```

4. **Try it out**
   - Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
   - Enter any English prompt, click **Generate**, and see LLM-based text in real-time!

***

##  Sample Prompts & Result

- **Prompt:** `The future of artificial intelligence is`
- **Generated:** 
  `The future of artificial intelligence is vast and unpredictable. As AI systems become more advanced, they will impact...`
- **Prompt:** `In the year 2050, cities will be powered by `
- **Generated:** 
  `In the year 2050, cities will be powered by wind and solar. But the cost of energy, and the climate impact...`
***

##  Customization

- **Change the Model:**  
  In `app.py`, replace `gpt2` with any other text-generation model supported by HuggingFace.
- **Improve Output Quality:**  
  Tune parameters like `max_length`, or use more powerful models such as `gpt2-medium`, `distilgpt2`, or others available on HuggingFace.

***

## 🌟 Learning Outcomes

- Understand HuggingFace pipeline APIs for text generation.
- Learn basic full-stack skills by connecting Python backends and static frontends.
- Practice deployment-readiness for GenAI-driven apps.

***
## Output 



***

##  Contributing

Feel free to fork, experiment, or open issues and pull requests to add features like summarization, sentiment analysis, cloud deployment, or new models!

***

## 📚 References

- [HuggingFace Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [GPT-2 Model Card](https://huggingface.co/gpt2)

***

**Created by Salila Punneshetty**  
*Inspired by curiosity for GenAI and its real-world potential.*  
*November 2025*

***
