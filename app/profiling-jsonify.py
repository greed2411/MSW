import json

def load_profile():
    with open('profiles.json', 'r') as infile:
        profiles = json.load(infile)

    return profiles

profile_details = {


            'shreyas' :
            {
                'name' : 'shreyas', 
                'projects_link' : '',            
                'cv_name' : '',
                'facebook_link' : '',
                'twitter_link' : '',
                'instagram_link' : '',
                'github_link' : '',
                'linkedin_link' : '',
                'mail_link' : 'mailto:',
                'content': 'I am a very simple sentence. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
            },
            
            'axel' :
            {
                'name' : 'axel', 
                'projects_link' : '',            
                'cv_name' : '',
                'facebook_link' : '',
                'twitter_link' : '',
                'instagram_link' : '',
                'github_link' : '',
                'linkedin_link' : '',
                'mail_link' : 'mailto:',
                'content': 'I am a very simple sentence. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
            },
            
            'joshua' :
            {
                'name' : 'joshua',
                'projects_link' : '',            
                'cv_name' : '',
                'facebook_link' : '',
                'twitter_link' : '',
                'instagram_link' : '',
                'github_link' : '',
                'linkedin_link' : '',
                'mail_link' : 'mailto:',
                'content': 'I am a very simple sentence. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'

            },
            
            'shaishav' :
            {
                'name' : 'shaishav', 
                'projects_link' : '',        
                'cv_name' : '',
                'facebook_link' : '',
                'twitter_link' : '',
                'instagram_link' : '',
                'github_link' : '',
                'linkedin_link' : '',
                'mail_link' : 'mailto:',
                'content': 'I am a very simple sentence. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
            },
            
            'aakriti' :
            {
                'name' : 'aakriti', 
                'projects_link' : '',            
                'cv_name' : '',
                'facebook_link' : '',
                'twitter_link' : '',
                'instagram_link' : '',
                'github_link' : '',
                'linkedin_link' : '',
                'mail_link' : 'mailto:',
                'content': 'I am a very simple sentence. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
            },
            
            'jaivarsan' :
            {
                'name' : 'jaivarsan',
                'projects_link' : 'https://github.com/greed2411?tab=repositories',            
                'cv_name' : 'jaivarsan',
                'facebook_link' : 'https://www.facebook.com/jaivarsan.bala',
                'twitter_link' : 'https://twitter.com/greed2411',
                'instagram_link' : '',
                'github_link' : 'https://github.com/greed2411',
                'linkedin_link' : 'https://www.linkedin.com/in/jaivarsan-b-50264b148/',
                'mail_link' : 'mailto:jaiimmortal@gmail.com',
                'content': 'I am a very simple sentence. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
            }

            
}

# UNCOMMENT THE BELOW TWO LINES AND RUN , WHEN YOU WANT TO SAVE NEW JSON FILE, I.E., UPDATED ARTICLE LIST.

# with open('profiles.json', 'w') as fp:
#     json.dump(profile_details, fp, indent=4)

profiles = load_profile()
# for profile_name in profiles:
#         name = profiles[profile_name]['name']
#         # it works.
#         print(name)

print(profiles['shreyas']['name'])