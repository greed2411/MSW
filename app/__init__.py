from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = 'supposed to be a secret'


@app.route('/about/')
def about():
    title = "About Us"
    content = "Team work mattters."
    return render_template('wrapper.html', title = title, content = content)


@app.route('/contact/')
def contact():
    title = "Contact Us"
    content = "Feel free to drop by and say hi."
    return render_template('wrapper.html', title = title, content = content)


@app.route('/')
def home_page():

    content = "Team work matters."
    return render_template('home.html', content = content)


@app.errorhandler(404)
def page_not_found(error):
    """
	for anyone trying different links or searching for images within the server
    """
    title = "404 bud."
    content = "what you are searching for isn't available."
    return render_template('wrapper.html', title = title, content = content), 404


@app.errorhandler(400)
def bad_request(error):

    title = "Aaaah ..."
    content = "Bad request, the server failed to help you."
    return render_template('wrapper.html' , title = title, content = content), 400


if __name__ == '__main__':

	app.run(debug = True)