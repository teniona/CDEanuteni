from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_bootstrap.html')


@app.route('/employee', methods=['POST'])
def employee():
    try:
        # extract employee data from request
        data = request.json
        first_name = data['first-name']
        last_name = data['last-name']
        age = data['age']
        currently_employed = data['currently-employed']

        # perform validation on the extracted data
        if not (first_name and last_name and age and currently_employed):
            # return an error response if any required field is missing
            return jsonify({'error': 'Invalid request data. Please make sure all required fields are included.'}), 400

        # do something with the validated employee data (e.g. save to database)

        # return a JSON response
        response = {'employee_name': f'{first_name} {last_name}', 'employee_age': age, 'employee_currently_employed': currently_employed}
        return jsonify(response)
    except KeyError:
        # handle KeyError if any of the required fields are missing
        return jsonify({'error': 'Invalid request data. Please make sure all required fields are included.'}), 400



if __name__ == '__main__':
    app.run()

