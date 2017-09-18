from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = 'supposed to be a secret'



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


# @app.route('/about/shreyas')
# @app.route('/about/axel')
# @app.route('/about/joshua')
# @app.route('/about/shaishav')
# @app.route('/about/aakriti')
# @app.route('/about/jaivarsan')


@app.route('/about/<name>')
def profile(name):
    if name in ['shreyas', 'axel', 'joshua', 'shaishav', 'aakriti', 'jaivarsan']:
        
        if name == 'shreyas':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link)
        
        elif name == 'axel':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link)

        elif name == 'joshua':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link)
        elif name == 'shaishav':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link)

        elif name == 'aakriti':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link)
                                                
        elif name == 'jaivarsan':
            projects_link = 'https://github.com/greed2411?tab=repositories'
            skills_link = ''
            cv_name = ''
            facebook_link = 'https://www.facebook.com/jaivarsan.bala'
            twitter_link = 'https://twitter.com/greed2411'
            instagram_link = ''
            github_link = 'https://github.com/greed2411'
            linkedin_link = ''
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link)

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