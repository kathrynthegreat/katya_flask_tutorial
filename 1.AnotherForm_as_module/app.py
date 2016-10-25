import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

# Initialize the Flask nyunyalication
nyunya = Flask(__name__)

# This is the path to the upload directory
dir = os.getcwd()
nyunya.config['UPLOAD_FOLDER'] = dir
# These are the extension that we are accepting to be uploaded
nyunya.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in nyunya.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@nyunya.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@nyunya.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(nyunya.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@nyunya.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(nyunya.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    nyunya.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True
    )

