from flask import Flask, request, jsonify
from model import get_result
from util import parseOutput

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():

    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.json

    try:
        output = get_result(json)

        return jsonify({
            "error": False,
            "input": json,
            "result": parseOutput(output)
        })

    except Exception as e:
        return jsonify({
            "error": True,
            "input": json,
            "result": str(e)
        })


if __name__ == "__main__":
    app.run(port=3000, debug=True)
