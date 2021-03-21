"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename

import os
from .forms import UploadForm
from flask import send_from_directory
from app import app, db
from app.models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mike Gold")


@app.route('/property', methods=['POST', 'GET'])
def property():
    """ For displaying the form to add a new property"""
    myform = UploadForm()
    # Validate file upload on submit
    print(request)
    if request.method == 'POST' and myform.validate_on_submit():
        # Get file data and save to your uploads folder
        photo = myform.upload.data
        filefolder = app.config['UPLOAD_FOLDER']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(filefolder,filename))
        flash('File Saved', 'success')

        title = myform.title.data
        bed = myform.bedroom.data
        bath = myform.bathroom.data
        loc = myform.location.data
        price = myform.price.data
        types = myform.types.data
        des = myform.description.data
        
        prop = Property (title, bed, bath, loc, price, types, des, filename)
        print(prop)
        db.session.add(prop)
        db.session.commit()
        flash('New user was successfully added')

        return redirect(url_for('properties'))
    return render_template('upload.html', form = myform)


@app.route('/properties')
def properties():
    """For displaying a list of all properties in the database."""
    files = get_uploaded_images()
    print(files)
    return render_template('files.html', files = files)


@app.route('/property/<propertyid>')
def get_image(propertyid):
    """For viewing an individual property by the specific property id."""
    rootdir = os.getcwd()
    filename = propertyid
    return send_from_directory(os.path.join(rootdir, app.config['UPLOAD_FOLDER']), filename)


def get_uploaded_images():
    rootdir = app.config['UPLOAD_FOLDER']
    print (rootdir)
    lst = []
    for _, _, files in os.walk(rootdir):
        for f in files:
            if len(f) > 3:
                if f[-3:] in ['jpg', 'png']:
                    lst.append(f)
    print(lst)
    return lst


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
