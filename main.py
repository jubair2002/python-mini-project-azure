from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Retrieve environment variable (e.g. set in Azure App Service Configuration)
    app_name = os.getenv("APP_NAME", "Default Flask App")
    environment = os.getenv("ENVIRONMENT", "Development")
    
    return f"""
    <h2>Welcome to {app_name}</h2>
    <p>Running in <strong>{environment}</strong> environment.</p>
    <p>This Flask app is deployed on Azure App Service 🚀</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
