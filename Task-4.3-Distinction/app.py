from flask import Flask
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "Development")
APP_MESSAGE = os.getenv("APP_MESSAGE", "Default Docker message")

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Docker Deployment - Task 4.3</title>
        </head>
        <body>
            <h1>Docker Web Application</h1>

            <h2>Task 4.3 - Distinction Level</h2>

            <p><strong>Student:</strong> Bhavana Mohan</p>
            <p><strong>Unit:</strong> SWE40006 Software Deployment and Evolution</p>

            <hr>

            <h3>Deployment Information</h3>
            <p><strong>Environment:</strong> {APP_ENV}</p>
            <p><strong>Deployment Message:</strong> {APP_MESSAGE}</p>

            <p>This Flask web application is containerized and deployed using Docker.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)