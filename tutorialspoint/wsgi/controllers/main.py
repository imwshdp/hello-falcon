import falcon

class MainController:
    def on_get(self, req, resp):
        resp.text = 'Hello World'
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT

    def on_post(self, req, resp):
      data=req.media
      nm=data['name']
      resp.text = 'Hello, ' + nm
      resp.status = falcon.HTTP_200
      resp.content_type = falcon.MEDIA_TEXT 