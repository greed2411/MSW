from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = 'supposed to be a secret'

@app.route('/about/')
def about():

    return render_template('about-contact.html')

@app.route('/contact/')
def contact():

    return "Contact us"



@app.route('/')
def home_page():
	"""
	Displaying homepage
	"""

	title = "YDL | YouTube Downloader"


	return render_template('index.html', title = title)


@app.errorhandler(404)
def page_not_found(error):
    """
	for anyone trying different links or searching for images within the server
    """
    return render_template('error_template.html' , title = "404 bud",
    												message = "Time to make the chimi-fuckin'-changas. ",
    												subline = "404, not there",
    												image_location = url_for('static', filename = 'images/deadpool-funny.jpg') ), 404


@app.errorhandler(400)
def bad_request(error):
	"""
	For handling situations where the server doesn't know what to do with the browser's request
	"""
	return render_template('error_template.html' , title = "Aaaah ...",
													message = "나는 이해하지 못한다.",
    												subline = "Yeah, the server couldn't understand what you asked for, Sorry",
    												image_location = url_for('static', filename = 'images/simpson-gangam.jpg')), 400


if __name__ == '__main__':

	app.run(debug = True)