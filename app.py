from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Mock app is running!"

@app.route("/get_sample_image", methods=["POST"])
def get_sample_image():
    data = request.json or {}
    query = data.get("query", "")
    return jsonify({
        "query_received": query,
        "image_url": "https://picsum.photos/400",
        "summary": "This is mock imagery returned for testing the ChatGPT integration."
    })

@app.route("/mcp", methods=["GET", "POST"])
def mcp_metadata():
    """Mock MCP metadata endpoint for ChatGPT connector discovery."""
    time.sleep(1)  # tiny delay helps prevent timeouts
    return jsonify({
        "name": "mock_eagleview_app",
        "version": "1.0.0",
        "tools": [
            {
                "name": "get_sample_image",
                "description": "Returns a mock property image and summary data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "User request or address text"
                        }
                    },
                    "required": ["query"]
                }
            }
        ]
    })

if __name__ == "__main__":
    app.run(port=5003)
