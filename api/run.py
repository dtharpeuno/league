import inspect
from flask import Flask, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from matrix_to_string import CSVFileToString

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

#routes
@app.route('/')
def health_check():
    return {'success': True}

@app.route("/echo", methods = ['POST'])
def upload_file():
    if not request.files:
        raise BadRequest('File upload is required')

    # should be file parameter from CURL
    file_data = request.files['file'].read().decode('utf-8')

    if file_data is None:
        raise BadRequest('Cannot read the data from uploaded file')

    # create instance obj from factory method
    matrix = CSVFileToString.create_matrix_object(
            file_data=file_data
        )

    # find all methods that will have on output
    # for iteration
    method_list = inspect.getmembers(
        matrix,
        predicate=inspect.ismethod
    )

    response_obj = {}
    for obj in method_list:
        if 'output' in obj[0]:
            output = obj[1]()
            response_obj[output.description] = output.data

    return response_obj


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)