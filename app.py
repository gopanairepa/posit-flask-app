from flask import Flask, jsonify, render_template_string
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Test App</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 60px auto; padding: 0 20px; background: #f5f5f5; }
        .card { background: white; border-radius: 8px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        h1 { color: #2d6a9f; }
        .badge { display: inline-block; background: #2d6a9f; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; }
        .endpoint { background: #f0f4f8; border-left: 4px solid #2d6a9f; padding: 10px 15px; margin: 10px 0; border-radius: 0 4px 4px 0; font-family: monospace; }
        a { color: #2d6a9f; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Flask Test App</h1>
        <p><span class="badge">Posit Connect</span> Deployment test — it's working!</p>
        <p><strong>Server time:</strong> {{ time }}</p>

        <h2>Available Endpoints</h2>
        <div class="endpoint"><a href="/api/health">GET /api/health</a> — Health check (JSON)</div>
        <div class="endpoint"><a href="/api/hello">GET /api/hello</a> — Hello world (JSON)</div>
        <div class="endpoint"><a href="/api/hello?name=World">GET /api/hello?name=...</a> — Personalized greeting</div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML, time=now)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.datetime.utcnow().isoformat()})

@app.route("/api/hello")
def hello():
    from flask import request
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!", "timestamp": datetime.datetime.utcnow().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)
