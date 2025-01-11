import falcon
import json

class ErrorsController:
    def on_get(self, req, resp):
       raise falcon.HTTPBadRequest(
         title="Value Out of Range",
         description="The value is not between permissible range"
      )