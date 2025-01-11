import falcon
import json

def check_input(req, resp, resource, params):
   student = json.load(req.bounded_stream)
   
   if "id" not in student:
      raise falcon.HTTPBadRequest(
         title="Bad request", description="Bad input, id must be provided."
      )
   
   if "name" not in student:
      raise falcon.HTTPBadRequest(
         title="Bad request", description="Bad input, name must be provided."
      )
   
   if "percent" not in student:
      raise falcon.HTTPBadRequest(
         title="Bad request", description="Bad input, percent must be provided."
      )

   percentage = int(student['percent'])
   if percentage < 0 or percentage > 100:
      raise falcon.HTTPBadRequest(
         title="Bad request", description="Bad input, invalid percentage"
      )
   
   req.context.data = student