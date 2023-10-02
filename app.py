from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

state = {"clicked": False, "displayName": ""}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/set-state", methods=["POST"])
def set_state():
    global state
    state["clicked"] = True
    date = datetime.now()
    state["displayName"] = str(date)
    app.logger.info('%s logged in successfully', str(date))
    # state["displayName"] = request.form.get("displayName", "")
    return jsonify({"message": "State set successfully"})

@app.route("/get-state")
def get_state():
    global state
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True)
