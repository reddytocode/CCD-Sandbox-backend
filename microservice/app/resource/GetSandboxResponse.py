from flask_restful import Resource, reqparse
import werkzeug
import logging
from ..controller.EpicBoxController import getProcessResponse, ResponseWrapper

parser = reqparse.RequestParser()
# parser.add_argument('password', help='This field cannot be blank', required=True)
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')


class GetSandboxResponse(Resource):

    def post(self):
        data = parser.parse_args()
        logging.warning(data)
        python_file = data['file'].stream.read()
        print(type(python_file))

        # response: ResponseWrapper = getProcessResponse(b'print(42)')
        response: ResponseWrapper = getProcessResponse(bytes(python_file))
        return {"output": str(response.output), "error": response.stderr}
        # return {"message": "holo"}
