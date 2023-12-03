
from flask import Flask, render_template, send_from_directory
from webserver import create_app

app = creat_app()

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
