import csv

from subprocess import call
from feed_compare import crawler, twitter
import random

#TODO: move this file to the feed_compare module directory and adjust import in app.py

bodies_path = 'athene_system/data/fnc-1/test_bodies.csv'
stances_path = 'athene_system/data/fnc-1/test_stances_unlabeled.csv'
result_path = 'athene_system/data/fnc-1/fnc_results/submission.csv'
'''
Hacky implementation which writes to csv instead to intercept the Athene submission process. Final product would properly implement the model.
'''

# 6 Media outlets chosen,
guardian_global = None
nytimes_global = None
bloomberg_global = None
thesun_global = None
foxnews_global = None
breitbart_global = None


def run_user_comparison(screen_name):
    timeline = twitter.get_timeline_urls(screen_name, 10)
    user_articles = [crawler.get_article(t) for t in timeline]
    user_headlines = [x[0] for x in user_articles]

    final_count = run_news_comparison(user_headlines)

    return(final_count)

def run_news_comparison(headlines):
    count = 100

    get_news_articles(count)

    global guardian_global
    global nytimes_global
    global bloomberg_global
    global thesun_global
    global foxnews_global
    global breitbart_global

    all_news = guardian_global + nytimes_global + bloomberg_global + thesun_global + foxnews_global + breitbart_global # Group articles into single list to run algorithm once.

    bodies = [x[1] for x in all_news]  #Take bodies from articles

    compare_headline(headlines, bodies)

    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        agree_count = 0
        disagree_count = 0
        discuss_count = 0

        reader_list = list(reader)

        final_count = []

        #TODO: Refactor the 6 iterations below.
        guardian_reader = reader_list[:len(guardian_global)]
        del(reader_list[:len(guardian_global)])
        for row in guardian_reader:
            if row[2] == 'agree':
                agree_count += 1
            if row[2] == 'disagree':
                disagree_count += 1
            if row[2] == 'discuss':
                discuss_count += 1
        #print("Guardian: Agree: {}, Disagree: {}, Discuss: {}".format(agree_count, disagree_count, discuss_count))
        final_count.append(("Guardian", agree_count, disagree_count, discuss_count))

        agree_count = 0
        disagree_count = 0
        discuss_count = 0
        nytimes_reader = reader_list[:len(nytimes_global)]
        del(reader_list[:len(nytimes_global)])
        for row in nytimes_reader:
            if row[2] == 'agree':
                agree_count += 1
            if row[2] == 'disagree':
                disagree_count += 1
            if row[2] == 'discuss':
                discuss_count += 1
        #print("NY Times: Agree: {}, Disagree: {}, Discuss: {}".format(agree_count, disagree_count, discuss_count))
        final_count.append(("NY Times", agree_count, disagree_count, discuss_count))

        agree_count = 0
        disagree_count = 0
        discuss_count = 0
        bloomberg_reader = reader_list[:len(bloomberg_global)]
        del(reader_list[:len(bloomberg_global)])
        for row in bloomberg_reader:
            if row[2] == 'agree':
                agree_count += 1
            if row[2] == 'disagree':
                disagree_count += 1
            if row[2] == 'discuss':
                discuss_count += 1
        #print("Bloomberg: Agree: {}, Disagree: {}, Discuss: {}".format(agree_count, disagree_count, discuss_count))
        final_count.append(("Bloomberg", agree_count, disagree_count, discuss_count))

        agree_count = 0
        disagree_count = 0
        discuss_count = 0
        thesun_reader = reader_list[:len(thesun_global)]
        del(reader_list[:len(thesun_global)])
        for row in thesun_reader:
            if row[2] == 'agree':
                agree_count += 1
            if row[2] == 'disagree':
                disagree_count += 1
            if row[2] == 'discuss':
                discuss_count += 1
        #print("The Sun: Agree: {}, Disagree: {}, Discuss: {}".format(agree_count, disagree_count, discuss_count))
        final_count.append(("The Sun", agree_count, disagree_count, discuss_count))

        agree_count = 0
        disagree_count = 0
        discuss_count = 0
        foxnews_reader = reader_list[:len(foxnews_global)]
        del(reader_list[:len(foxnews_global)])
        for row in foxnews_reader:
            if row[2] == 'agree':
                agree_count += 1
            if row[2] == 'disagree':
                disagree_count += 1
            if row[2] == 'discuss':
                discuss_count += 1
        #print("Fox News: Agree: {}, Disagree: {}, Discuss: {}".format(agree_count, disagree_count, discuss_count))
        final_count.append(("Fox News", agree_count, disagree_count, discuss_count))

        agree_count = 0
        disagree_count = 0
        discuss_count = 0
        breitbart_reader = reader_list[:len(breitbart_global)]
        del(reader_list[:len(breitbart_global)])
        for row in breitbart_reader:
            if row[2] == 'agree':
                agree_count += 1
            if row[2] == 'disagree':
                disagree_count += 1
            if row[2] == 'discuss':
                discuss_count += 1
        #print("Brietbart: Agree: {}, Disagree: {}, Discuss: {}".format(agree_count, disagree_count, discuss_count))
        final_count.append(("Breitbart", agree_count, disagree_count, discuss_count))

    #print(final_count)
    return final_count


def get_news_articles(count):
    global guardian_global
    global nytimes_global
    global bloomberg_global
    global thesun_global
    global foxnews_global
    global breitbart_global

    if guardian_global is None:
        timeline = twitter.get_timeline_urls('guardian', count)
        guardian_global = [crawler.get_article(t) for t in timeline]
    if nytimes_global is None:
        timeline = twitter.get_timeline_urls('nytimes', count)
        nytimes_global = [crawler.get_article(t) for t in timeline]
    if bloomberg_global is None:
        timeline = twitter.get_timeline_urls('Bloomberg', count)
        bloomberg_global = [crawler.get_article(t) for t in timeline]
    if thesun_global is None:
        timeline = twitter.get_timeline_urls('TheSun', count)
        thesun_global = [crawler.get_article(t) for t in timeline]
    if foxnews_global is None:
        timeline = twitter.get_timeline_urls('FoxNews', count)
        foxnews_global = [crawler.get_article(t) for t in timeline]
    if breitbart_global is None:
        timeline = twitter.get_timeline_urls('BreitbartNews', count)
        breitbart_global = [crawler.get_article(t) for t in timeline]


def compare_headline(headlines, bodies=None):
    '''
    headline: a single headline string to compare
    bodies: a list of body strings with which to compare the headline
    '''

    if bodies is not None:
        with open(bodies_path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Body ID', 'articleBody'])
            index = 0
            for b in bodies:
                index+=1
                writer.writerow([index] + [b])

    with open(stances_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Headline', 'Body ID'])
        index = 0
        for x in range(1,len(bodies)+1):
            writer.writerow([random.choice(headlines), x])

    print('Finished writing CSV files, running model...')
    call(['python','athene_system/fnc/pipeline.py', '-p', 'ftest'])


if __name__ == '__main__':
    test_user = 'seanhannity'
    print(run_user_comparison(test_user))
