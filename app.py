from waitress import serve
from common import app

if __name__ == "__main__":
    print("Serving on http://localhost:4040")
    serve(app, host="0.0.0.0", port=4040)
