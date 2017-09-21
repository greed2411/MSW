from flask import Flask, render_template, redirect, url_for, abort
import json

app = Flask(__name__)
app.secret_key = 'supposed to be a secret'

def load_articles():
    with open('articles.json', 'r') as infile:
        articles = json.load(infile)

    return articles

def load_profile():
    with open('profiles.json', 'r') as infile:
        profiles = json.load(infile)

    return profiles

@app.route('/')
def home_page():

    return render_template('home.html')

@app.route('/about/')
def about():
    title = "About Us"
    content = "Team work matters."
    return render_template('about.html', title = title, content = content)


@app.route('/contact/')
def contact():
    title = "Contact Us"
    content = "Feel free to drop by and say hi."
    return render_template('contact.html', title = title, content = content)


@app.route('/blog/')
def blog():
    title = "Motus Simulation Blog"
    articles = load_articles()
    return render_template('blog.html', title = title, articles = articles, blog_home = True)


@app.route('/about/<name>')
def profile(name):

    profiles = load_profile()
    if name in ['shreyas', 'axel', 'joshua', 'shaishav', 'aakriti', 'jaivarsan']:
        if name == 'shreyas':
            profile = profiles['shreyas']
        
        elif name == 'axel':
            profile = profiles['axel']

        elif name == 'joshua':
            profile = profiles['joshua']

        elif name == 'shaishav':
            profile = profiles['shaishav']

        elif name == 'aakriti':
            profile = profiles['aakriti']
                                                
        elif name == 'jaivarsan':
            profile = profiles['jaivarsan']

        return render_template('profile.html', profile = profile)
    
    else:

        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    """
	for anyone trying different links or searching for images within the server
    """
    title = "404 bud."
    content = "what you are searching for isn't available."
    return render_template('error.html', title = title, content = content), 404


@app.errorhandler(400)
def bad_request(error):

    title = "Aaaah ..."
    content = "Bad request, the server failed to help you."
    return render_template('error.html' , title = title, content = content), 400


if __name__ == '__main__':

	app.run(debug = True)