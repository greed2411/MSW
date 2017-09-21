import json

def load_articles():
    with open('articles.json', 'r') as infile:
        articles = json.load(infile)

    return articles


article_details_dictionary = {

            # IMPORTANT : new articles first, so place the new article above the existing articles.
            '18-09-2017' :
            {
                'title':"Phase 2 of Arm robot", # title_of_the_article
                'publishedDate':"Monday, September 18, 2017", # published_date - maintain this format - day_of_the_week, month date_of_the_month, year
                'authors':"Shreyas Sharma, Axel", # author_of_post
                'urlLink':"phase-2-of-arm-robot", # the html page of the title mentioned, maintain this format.
                'tags':["research", "application", "sensors", "IoT"] # all the tags you want for the article.
            }, # remember the comma ',' after every line
            '13-09-2017' :
            {
                'title':"Phase 1 of Arm robot", # title_of_the_article
                'publishedDate':"Wednesday, September 13, 2017", # published_date - maintain this format - day_of_the_week, month date_of_the_month, year
                'authors':"Shreyas Sharma, Axel", # author_of_post
                'urlLink':"phase-1-of-arm-robot", # the html page of the title mentioned, maintain this format.
                'tags':["research", "bioinspiration", "OpenSim"] # all the tags you want for the article.
             } # remember the comma ',' after every line
            
}

# UNCOMMENT THE BELOW TWO LINES AND RUN , WHEN YOU WANT TO SAVE NEW JSON FILE, I.E., UPDATED ARTICLE LIST.

# with open('articles.json', 'w') as fp:
#     json.dump(article_details_dictionary, fp, indent=4)

# articles = load_articles()
# for article_date in articles:
#         title = articles[article_date]['title']
#         publishedDate = articles[article_date]['publishedDate']
#         authors = articles[article_date]['authors']
#         urlLink = articles[article_date]['urlLink']
#         tags = articles[article_date]['tags']


