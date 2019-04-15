
from flask import Flask, request, render_template
from main import move_filtered_files

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data')
def get_data():
    source_dir = request.args.get('input1')
    target_dir = request.args.get('input2')
    filter_str = request.args.get('input3')
    try:
        move_filtered_files(source_dir, target_dir, filter_str)
    except:
        return 'Something went wrong'
    return 'Files moved successfully'
    

if __name__ == '__main__':
    app.run(debug=True)
