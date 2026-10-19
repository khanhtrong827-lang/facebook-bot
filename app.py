from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><meta charset='utf-8'><title>Chuc 20-10</title></head>
    <body style="text-align:center; font-family:Arial; margin-top:50px">
    <h1 style="color:#e91e63">Chuc Mung 20-10</h1>
    <h2>Website dang chay 24/24 - Tat may van chay!</h2>
    <p>Link nay la link www cua ban do!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
