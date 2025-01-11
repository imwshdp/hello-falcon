import falcon
import json

class ParameterController:
    def on_get(self, req, resp, name, age):
        # resp.text = f'Hello {name} with {age} years old'
        # resp.status = falcon.HTTP_200
        # resp.content_type = falcon.MEDIA_TEXT

        return_value={ "name": name, "age": age }
        resp.text=json.dumps(return_value)

        resp.status = falcon.HTTP_200 
        resp.content_type = falcon.MEDIA_JSON
