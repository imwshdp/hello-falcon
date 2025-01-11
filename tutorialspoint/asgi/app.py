import uvicorn
import falcon.asgi

from controllers.main import MainController
from controllers.jinja import JinjaController

app = falcon.asgi.App()

app.add_route('/', MainController())
app.add_route('/jinja', JinjaController())

if __name__ == "__main__":
   uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)