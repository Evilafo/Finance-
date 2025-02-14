from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Variables globales pour simuler le marché
midpoint = 10.0
spread = 2.0
bid = midpoint - spread / 2
offer = midpoint + spread / 2

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update_market", methods=["POST"])
def update_market():
    global midpoint, spread, bid, offer
    data = request.json
    midpoint = float(data.get("midpoint", midpoint))
    spread = float(data.get("spread", spread))
    bid = midpoint - spread / 2
    offer = midpoint + spread / 2
    return jsonify({"bid": bid, "offer": offer})

@app.route("/get_market", methods=["GET"])
def get_market():
    return jsonify({"bid": bid, "offer": offer})

if __name__ == "__main__":
    app.run(debug=True)
