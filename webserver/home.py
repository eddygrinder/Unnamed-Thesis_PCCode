from website import create_app
from flask import send_from_directory

app = create_app()

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory("images", filename)

# Definição dos bits a serem transmitidos


if __name__ == '__main__':
    app.run(debug=True)
