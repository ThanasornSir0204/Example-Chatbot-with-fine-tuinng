# Chatbot Text Classification

This is a simple chatbot that analyzes text and classifies its sentiment (positive/negative) using a pre-trained model from Hugging Face Transformers.

## Features
- Uses `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis.
- Identifies whether the input text is **positive** or **negative**.
- Provides a confidence score for the classification.
- Interactive chatbot interface in the terminal.

## Installation
### Prerequisites
Make sure you have Python installed (Python 3.7+ recommended). You will also need the `transformers` and `torch` libraries.

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```sh
   pip install transformers torch
   ```
3. Run the chatbot:
   ```sh
   python chatbot.py
   ```

## Usage
Once you run the script, the chatbot will prompt you to enter a message. Type any text, and it will classify the sentiment:
```
Chatbot: Hello! You can type a message, and I'll tell you what it's about.
You: I love this product!
Chatbot: I think you're talking about POSITIVE (Confidence: 0.98)
```
To exit, type `exit`, `quit`, or `bye`.

## Customization
If you want to use a multilingual model, you can replace the model with:
```python
classifier = pipeline("text-classification", model="joeddav/xlm-roberta-large-xnli")
```
This supports over **100 languages**.

## License
This project is licensed under the MIT License.

---
Feel free to modify and improve the chatbot as needed!

