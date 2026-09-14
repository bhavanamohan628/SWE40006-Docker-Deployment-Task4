from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Docker Flask Application</h1>
    <p>SWE40006 Software Deployment and Evolution</p>
    <p>Task 4.2 - Credit Level</p>
    <p>The application is successfully running inside a Docker container.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)