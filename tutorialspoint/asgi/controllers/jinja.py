import falcon

from helpers.get_template import load_template

class JinjaController:
    async def on_get(self, req, resp):
        template = load_template('index.html')

        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.text = template.render()