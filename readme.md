This app currently takes a Twitter user's news feed and evaluates the extent to which the articles they share agree or disagree with articles published by six major news outlets.

It uses a classification algorithm developed by UKP Lab (https://github.com/hanselowski/athene_system)


==================================

Local installation (Mac/Unix):
------------
Install python3.
Clone this repository.
Create virtual environment.
> ```
> python3 -m venv myvenv
> source venv/bin/activate
> ```

Install requirements.
> ```
> git clone "https://github.com/hanselowski/athene_system.git"
> python3 pip install -r requirements.txt
> ```

Edit feed_compare/tokens_SKELETON.py to include relevant Twitter tokens (Consumer Key, Secret, and Access Token), and rename to tokens.py.

Unzip the [features](https://drive.google.com/open?id=0B0-muIdcdTp7UWVyU0duSDRUd3c) file to the directory:
> ```
>athene_system/data/fnc-1/features
> ```

Unzip the [model](https://drive.google.com/open?id=0B0-muIdcdTp7Sm42ZW1yUndyY1E) file to the directory:
> ```
>athene_system/data/fnc-1/mlp_models
> ```

Parts of the Natural Language Toolkit (NLTK) might need to be installed manually:
> ```
> python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"
> ```

Optional:
Copy [Word2Vec GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) to folder athene_system/data/embeddings/google_news/.


Optional:
Download [Paraphrase Database: Lexical XL Paraphrases 1.0](http://www.cis.upenn.edu/~ccb/ppdb/release-1.0/ppdb-1.0-xl-lexical.gz) and extract it to the athene_system/data/ppdb folder.


==================================

To run:
------------
> ```
> python app.py
> ```

Browse to http://localhost:5001/
