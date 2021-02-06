from app.api import bp
import gensim.downloader as api

word_vectors = api.load("glove-wiki-gigaword-100")

@bp.route('/similarity-search/<string:searchTerm>')
def search_feeds(searchTerm):
    