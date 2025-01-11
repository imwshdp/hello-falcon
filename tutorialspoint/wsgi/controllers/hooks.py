import falcon
import json

from data.students import students
from hooks.validator import check_input

class HooksController:
    def on_get(self, req, resp):
        resp.text = json.dumps(students)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON

    @falcon.before(check_input)
    def on_post(self, req, resp):
        student = json.load(req.context.data)
        students.append(student)

        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "Student added successfully."

    def on_get_student(self, req, resp, id):
        resp.text = json.dumps(students[id-1])

        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON