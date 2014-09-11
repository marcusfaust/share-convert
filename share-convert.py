import os
from flask import Flask, send_from_directory, render_template, request, flash
from uploadhandler import uploadedCSV


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        server = request.form['server']
        mountpoint = request.form['path']
        if file:
            file.save('tmp.csv')
            tempfile = uploadedCSV(file)
            tempOutput = tempfile.outputCmds(server, mountpoint)
            os.remove('tmp.csv')

            return render_template('output.html', tempOutput=tempOutput)

    return render_template('upload.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True)
