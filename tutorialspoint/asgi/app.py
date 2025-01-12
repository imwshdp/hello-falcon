import uvicorn
import falcon.asgi

from controllers.main import MainController
from controllers.jinja import JinjaController
from controllers.ws import WebSocketResource

from middlewares.main import MyMiddleware

app = falcon.asgi.App(
   middleware=[
      MyMiddleware(),
      falcon.CORSMiddleware(allow_origins='*', allow_credentials='*')
   ],
   # cors_enable = True
)

app.add_route('/', MainController())
app.add_route('/jinja', JinjaController())
app.add_route('/ws', WebSocketResource())

if __name__ == "__main__":
   print('Serving on http://localhost:8000')
   uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)