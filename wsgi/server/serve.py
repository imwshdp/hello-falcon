import waitress

from server.app import get_app

app = get_app()

def serve():
    waitress.serve(app, host='0.0.0.0', port=8000)