# EagleView-Mock-App

# 🛰️ EagleView Mock App

A lightweight **Flask-based mock backend** used to simulate EagleView’s integration with the **ChatGPT Marketplace App (Apps SDK)**.  
This proof-of-concept demonstrates how ChatGPT could communicate with an external geospatial app through a simple **MCP (Model Context Protocol)** endpoint.

---

## 📘 Overview

This mock app simulates what a real EagleView–ChatGPT integration could look like.  
It doesn’t call internal services or APIs — instead, it provides **mock responses** to mimic data flow and app discovery behavior.

The app exposes three key routes:

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Health check endpoint (returns “✅ Mock app is running!”) |
| `/get_sample_image` | POST | Returns mock property image and summary data for testing integration |
| `/mcp` | GET / POST | Returns metadata that ChatGPT uses to discover app tools and schema |

---

## 🧠 Code Summary

### `app.py`
Main Flask application.  
Defines endpoints and returns JSON responses for testing integration. 

### `ai-plugin.json`
Manifest file describing the app to ChatGPT (used for connector discovery).

### `openai.yaml`
Defines the OpenAPI schema for `/get_sample_image`.

## ⚙️ Commands

### 1️⃣ Setup environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors

python app.py

ngrok http 5003

or alternatively

npx cloudflared tunnel --url http://localhost:5003


## Integration with ChatGPT (Apps SDK)

Enable Developer Mode in ChatGPT.

Go to Settings → Connectors → Create.

Use the public tunnel URL (from ngrok or Cloudflare) ending in /mcp.

Choose No authentication.

Click Create.

If successful, ChatGPT should detect the get_sample_image tool and allow queries like:

“Show me a sample roof image for Seattle.”

## ⚠️ Known Issue (Current Blocker)

ChatGPT currently times out during connector creation, even though the mock app responds with valid MCP metadata.

✅ Verified

Flask logs show:

POST /mcp HTTP/1.1" 200 -


/mcp endpoint tested successfully via Postman and browser

Public HTTPS tunnels (ngrok + Cloudflare) confirmed reachable

🧩 Root cause

This appears to be a ChatGPT Apps SDK beta limitation — intermittent timeouts during connector validation, especially when using free or temporary tunnels.
