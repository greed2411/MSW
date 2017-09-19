from flask import Flask, render_template, redirect, url_for

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


@app.route('/about/<name>')
def profile(name):

    # list_of_members = ['shreyas', 'axel', 'joshua', 'shaishav', 'aakriti', 'jaivarsan']
    
    # if name in list_of_members:
    #     position = list_of_members.index(name)

    # member_details{
    #     0 : [

    #     ],
    #     1 : [

    #     ],
    #     2 : [

    #     ],
    #     3 : [

    #     ],
    #     4 : [

    #     ],
    #     5 : [

    #     ]
    # }
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
            mail_link = 'mailto:'
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link,
                                                mail_link = mail_link)
        
        elif name == 'axel':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            mail_link = 'mailto:'
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link,
                                                mail_link = mail_link)

        elif name == 'joshua':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            mail_link = 'mailto:'
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link,
                                                mail_link = mail_link)
        elif name == 'shaishav':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            mail_link = 'mailto:'
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link,
                                                mail_link = mail_link)

        elif name == 'aakriti':
            projects_link = ''
            skills_link = ''
            cv_name = ''
            facebook_link = ''
            twitter_link = ''
            instagram_link = ''
            github_link = ''
            linkedin_link = ''
            mail_link = 'mailto:'
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link,
                                                mail_link = mail_link)
                                                
        elif name == 'jaivarsan':
            projects_link = 'https://github.com/greed2411?tab=repositories'
            skills_link = ''
            cv_name = 'jaivarsan'
            facebook_link = 'https://www.facebook.com/jaivarsan.bala'
            twitter_link = 'https://twitter.com/greed2411'
            instagram_link = ''
            github_link = 'https://github.com/greed2411'
            linkedin_link = 'https://www.linkedin.com/in/jaivarsan-b-50264b148/'
            mail_link = 'mailto:jaiimmortal@gmail.com'
            return render_template('profile.html', 
                                                name = name, 
                                                projects_link = projects_link, 
                                                skills_link = skills_link, 
                                                cv_name = cv_name, 
                                                facebook_link = facebook_link, 
                                                twitter_link = twitter_link,
                                                instagram_link = instagram_link, 
                                                github_link = github_link, 
                                                linkedin_link = linkedin_link,
                                                mail_link = mail_link)

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