import falcon
import json

class CookiesController:
    def on_get(self, req, resp):
        cookie_values = req.get_cookie_values('user')
        if cookie_values:
            first_value = cookie_values[0]
            resp.text = json.dumps({ "user": first_value })
            resp.unset_cookie('user')
        else:
            resp.set_cookie("user", 'admin')
            resp.text = "cookie set successfully."

        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT
