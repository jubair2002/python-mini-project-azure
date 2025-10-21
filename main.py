from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve environment variables directly from Azure App Service
    app_name = os.getenv("APP_NAME")           # e.g. set in Azure App Settings
    environment = os.getenv("ENVIRONMENT")     # e.g. "Production" or "Staging"
    version = os.getenv("APP_VERSION")         # optional, can store version

    # Handle if not found
    if not app_name:
        app_name = "APP_NAME not set"
    if not environment:
        environment = "ENVIRONMENT not set"
    if not version:
        version = "APP_VERSION not set"

    return f"""
    <html>
    <head><title>{app_name}</title></head>
    <body style="font-family: Arial; margin: 40px;">
        <h2>Welcome to {app_name}</h2>
        <p>Environment: <strong>{environment}</strong></p>
        <p>Version: <strong>{version}</strong></p>
        <p>✅ Environment variables are being read from Azure App Service.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Azure expects to listen on 0.0.0.0 with dynamic port if provided
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
