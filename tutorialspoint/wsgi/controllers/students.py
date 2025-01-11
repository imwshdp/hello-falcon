import falcon
import json

from data.students import students

class StudentsController:
    def on_get(self, req, resp):
        resp.text = json.dumps(students)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON

    def on_post(self, req, resp):
        student = json.load(req.bounded_stream)
        students.append(student)

        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "Student added successfully."

    def on_get_student(self, req, resp, id):
        resp.text = json.dumps(students[id-1])
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON

    def on_put_student(self, req, resp, id):
        student=students[id-1]
        data = json.load(req.bounded_stream)

        student.update(data)
        resp.text = json.dumps(student)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON

    def on_delete_student(self, req, resp, id):
        students.pop(id-1)
        resp.text = json.dumps(students)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON

       