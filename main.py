import flask


# TODO: change this to your academic email
AUTHOR = "andrewzx@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password too long"})
    
    return flask.jsonify({"valid": True, "reason": ""}), 200
    
