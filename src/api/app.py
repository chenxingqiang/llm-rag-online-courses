from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the LLM-RAG Online Course API"

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    # Process the query using your LLM-RAG model here
    response = {"result": "This is a placeholder response"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)