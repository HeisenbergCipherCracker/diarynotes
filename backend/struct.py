import os
from flask import Flask, render_template
from backend.settings import INDEX_HTML_PATH

# Assuming INDEX_HTML_PATH is the filename, not a full path

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    with open(INDEX_HTML_PATH,'r') as file:
        content = file.read()
    return render_template(content)

def runner():
    app.run(debug=True)

# Run the Flask app

