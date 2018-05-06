import newspaper
from newspaper import Article

def get_article(article_url):
    try:
        article = Article(article_url, fetch_images=False)
        article.download() #TODO: Fix truncated article text
        article.parse()
        title = article.title
        text = article.text
    except:
        return('','')
    return(title, text)

def get_newspaper():
    cnn_paper = newspaper.build('http://cnn.com')
    for article in cnn_paper.articles:
        print(article.title)
    return


if __name__ == '__main__':

    a = get_article('https://cnn.it/2FMGxvD')
    print(a[0])

    get_newspaper()
