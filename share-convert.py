import os
from flask import Flask, send_from_directory, render_template, request, flash

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['myfile']
        if file:
            file.save('/tmp', 'tmp.csv')
            flash("Processing File")

    return render_template('upload.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True)
