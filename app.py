from flask import Flask
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve environment variables from Azure App Service
    app_name = os.getenv("APP_NAME") or "APP_NAME not set"
    environment = os.getenv("ENVIRONMENT") or "ENVIRONMENT not set"
    version = os.getenv("APP_VERSION") or "APP_VERSION not set"

    # Try to get database connection string from Azure
    db_conn_str = os.getenv("db_cred")

    db_status = "❌ Database connection string not found."

    if db_conn_str:
        try:
            # You can parse manually or hardcode your credentials for test
            # Example format: Server=server;Database=db;Uid=user;Pwd=pass;
            parts = dict(item.split('=') for item in db_conn_str.split(';') if item)
            conn = mysql.connector.connect(
                host=parts.get('Server'),
                user=parts.get('Uid'),
                password=parts.get('Pwd'),
                database=parts.get('Database')
            )
            if conn.is_connected():
                db_status = "✅ Database Connected Successfully!"
                conn.close()
        except Error as e:
            db_status = f"❌ Database Connection Failed: {e}"

    return f"""
    <html>
    <head><title>{app_name}</title></head>
    <body style="font-family: Arial; margin: 40px;">
        <h2>Welcome to {app_name}</h2>
        <p>Environment: <strong>{environment}</strong></p>
        <p>Version: <strong>{version}</strong></p>
        <hr>
        <p><strong>Database Status:</strong> {db_status}</p>
        <p>✅ Environment variables are being read from Azure App Service.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Azure expects to listen on 0.0.0.0 with dynamic port if provided
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
