import falcon

from helpers.get_template import load_template

class WebSocketResource:
    async def on_get(self, req, resp):
        template = load_template('websocket.html')

        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.text = template.render()

    async def on_websocket(self, req, websocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")