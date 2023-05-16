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

        # do something with the employee data (e.g. save to database)
        # ...

        # return a JSON response
        response = {'employee_name': f'{first_name} {last_name}', 'employee_age': age, 'employee_currently_employed': currently_employed}
        return jsonify(response)
    except KeyError:
        return jsonify({'error': 'Invalid request data. Please make sure all required fields are included.'}), 400




if __name__ == '__main__':
    app.run()

