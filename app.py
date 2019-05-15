
from flask import Flask, request, render_template
from main import move_filtered_files

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def get_data():
    """Args is a dict, we are using the get method instead of the [] 
       so that it will return 'none' if key is missing/undefined."""
    data = request.form
    source_dir = data.get('input1')
    target_dir = data.get('input2')
    filter_str = data.get('input3')
    try:
        # move_filtered_files(source_dir, target_dir, filter_str)
        return '{source}, {target}, {filter}' \
            .format(source=source_dir, target=target_dir, filter=filter_str)
    except:
        return 'Something went wrong'
    # return 'Files moved successfully'
    

if __name__ == '__main__':
    app.run(debug=True)
