from flask import Flask, request, jsonify
from model import predict
from util import parseInput

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():

    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.json
        input = parseInput(json)

    try:
        output = predict(input)

        return jsonify({
            "error": False,
            "input": json,
            "result": output
        })

    except Exception as e:
        return jsonify({
            "error": True,
            "input": json,
            "result": str(e)
        })


if __name__ == "__main__":
    app.run(port=3000, debug=True)
