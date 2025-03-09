from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
@app.route('/')
def home():
    return "Mentrabot is running!"
# Set your OpenAI API key
openai.api_key = "your-api-key-here"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
