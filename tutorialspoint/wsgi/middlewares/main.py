class MyMiddleware:
   def process_request(self, req, resp):
      pass
   def process_resource(self, req, resp, resource, params):
      pass
   def process_response(self, req, resp, resource, req_succeeded):
      pass