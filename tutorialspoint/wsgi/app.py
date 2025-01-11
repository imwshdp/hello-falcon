from wsgiref.simple_server import make_server
from waitress import serve
import falcon

from controllers.main import MainController
from controllers.parameter import ParameterController
from controllers.students import StudentsController
from controllers.cookies import CookiesController
from controllers.errors import ErrorsController
from controllers.hooks import HooksController

app = falcon.App()

app.add_route('/', MainController())

app.add_route('/with/{name}/{age:int}', ParameterController())

app.add_route("/students", StudentsController())
app.add_route("/students/{id:int}", StudentsController(), suffix='student')

app.add_route("/cookies", CookiesController())
app.add_route("/errors", ErrorsController())
app.add_route("/hooks", HooksController())

if __name__ == '__main__':
    print('Serving on port 8000')

    # """wsgiref serving"""
    # with make_server('', 8000, app) as httpd:
    #     # Serve until process is killed
    #     httpd.serve_forever()

    # """waitress serving"""
    serve(app, host='127.0.0.1', port=8000)