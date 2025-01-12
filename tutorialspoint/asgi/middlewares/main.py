class MyMiddleware:
   async def process_startup(self, scope, event):
      pass
   async def process_shutdown(self, scope, event):
      pass
   async def process_request(self, req, resp):
      pass
   async def process_resource(self, req, resp, resource, params):
      pass
   async def process_response(self, req, resp, resource, req_succeeded):
      pass
   async def process_request_ws(self, req, ws):
      pass
   async def process_resource_ws(self, req, ws, resource, params):
      pass