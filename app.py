from flask import Flask, request, jsonify
import threading
import time
import requests

from producer import send_item

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "RouteMobile Assignment API"})



@app.route("/items", methods=["POST"])
def add_item():

    data = request.get_json()

    if not data or "item" not in data:
        return jsonify({"error": "item is required"}), 400

    send_item(data["item"])

    return jsonify({
        "message": "Item accepted successfully"
    }), 202



def hit_httpbin(delay):

    url = f"https://httpbin.org/delay/{delay}"

    try:
        requests.get(url)
    except Exception:
        pass



@app.route("/delay", methods=["GET"])
def delay():

    delay_value = request.args.get(
        "delay_value",
        type=int
    )

    if delay_value is None:
        return jsonify({
            "error": "delay_value is required"
        }), 400

    threads = []

    start = time.time()

    for _ in range(5):
        t = threading.Thread(
            target=hit_httpbin,
            args=(delay_value,)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()

    return jsonify({
        "time_taken": round(end - start, 2)
    }), 200


if __name__ == "__main__":
    app.run(debug=True)