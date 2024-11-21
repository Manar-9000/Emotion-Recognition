from flask import Flask, request, jsonify
import text2emotion as te

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    text = data.get('text', '')
    emotions = te.get_emotion(text)
    return jsonify(emotions)

if __name__ == "__main__":
    app.run(debug=True)
