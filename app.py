from flask import Flask, jsonify

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "Welcome to PR POC Demo Application"

# Health Check Route
@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "pr-poc-demo",
        "version": "1.0.0"
    })

# Version Route
@app.route("/version")
def version():
    return jsonify({
        "application": "PR POC Demo",
        "version": "1.0.0"
    })

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Resource not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)

