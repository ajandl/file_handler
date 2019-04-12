
from flask import Flask, request
from main import move_filtered_files

app = Flask(__name__)


@app.route('/')
def hello_world():
    return (
        '<form action="http://localhost:5000/data"><input name="input1" type="text" /><input type="submit" /></form>'
    )

@app.route('/data')
def get_data():
    data = request.args.get('input1')
    return f'Got the data: {data}'


if __name__ == '__main__':
    app.run(debug=True)
