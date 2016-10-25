from Form import app
from Form import database_helper 

import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename


# Initialize the Flask application
#app = Flask(__name__)

'''
@app.route('/')
def index():
    return 'Hello World!'
'''

# This is the path to the upload directory
dir = os.getcwd()
app.config['UPLOAD_FOLDER'] = dir

# These are the extension that we are accepting to be uploaded for photos
app.config['ALLOWED_EXTENSIONS'] = set(['pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))


@app.route("/csvupload", methods=['POST'] )
def csv_upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)      
        #pull the path out where the file is downloaded
        f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #save the file
        file.save(f)
        #upload the file to the database using our upload() metheod
        database_helper.upload(f)
        #with a csv there's nothing to display but your still need the redirect
        return redirect(url_for('uploaded_file',   filename=filename))
        #return 'OK Loading to DB'

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)    
    #database_helper.upload(os.path.join(app.config['UPLOAD_FOLDER'], filename))



'''
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True
    )
'''