from flask import Flask, jsonify, request
import time

# create a Flask web application instance
app = Flask(__name__)

@app.route("/")
def home():
    # root endpoint that confirms the mock app is running
    return "Mock app is running!"

@app.route("/get_sample_image", methods=["POST"])
def get_sample_image():
    # endpoint to simulate fetching a sample image given a query
    # it expects a JSON request with an optional "query" field
    data = request.json or {}  
    query = data.get("query", "")  # extract query text or use empty string
    # return mock data including a placeholder image and a short summary
    return jsonify({
        "query_received": query,
        "image_url": "https://picsum.photos/400",  # random image URL
        "summary": "This is mock imagery returned for testing the ChatGPT integration."
    })

@app.route("/mcp", methods=["GET", "POST"])
def mcp_metadata():
    """
    Mock MCP (Model Context Protocol) metadata endpoint.
    Used by ChatGPT or similar connectors to discover available tools.
    """
    time.sleep(1)  # small delay to simulate real network latency and avoid timeouts
    # return metadata about this mock application and the available tools
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

# run the app locally on port 5003 when this file is executed directly
if __name__ == "__main__":
    app.run(port=5003)
