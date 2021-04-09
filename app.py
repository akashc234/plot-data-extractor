import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, make_response
from werkzeug import secure_filename
from predict import predictor
import pandas as pd 

UPLOAD_FOLDER = os.path.join('static', 'img')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        global xmax
        xmax = request.form['xmax']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'current.png'))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')

@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = '/uploads/' + filename
    return render_template('index.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, 'current.png')

@app.route('/result', methods=['GET', 'POST'])
def result():
    final_result = predictor(xmax)
    L = []
    for key in final_result:
        for values in final_result[key]:
            L.append([values[0], values[1], key])
    df = pd.DataFrame(L, columns = ['X', 'Y', 'Colors'])
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp     

if __name__ == '__main__':
    app.run(debug = True)