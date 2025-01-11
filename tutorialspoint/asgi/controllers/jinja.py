import os
import falcon
import jinja2

def load_template(name):
    path = os.path.join('../templates', name)
    with open(os.path.abspath(path), 'r') as fp:
        return jinja2.Template(fp.read())

class JinjaController:
    async def on_get(self, req, resp):
        template = load_template('index.html')
        rendered_template = template.render()
        
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = rendered_template