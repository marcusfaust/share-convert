import os
from flask import Flask, send_from_directory, render_template, request, flash
from uploadhandler import uploadedCSV


app = Flask(__name__)
app.secret_key = 'some_secret'


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
        file = request.files['file']
        server = request.form['server']
        mountpoint = request.form['path']
        if file:
            file.save('tmp.csv')
            tempfile = uploadedCSV(file)
            tempOutput = tempfile.outputCmds(server, mountpoint)
            return render_template('output.html')

    return render_template('upload.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True)
