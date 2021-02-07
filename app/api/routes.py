from app.api import bp
from app import db
from app.models import RssChannel
import gensim.downloader as api
from sqlalchemy import inspect 


# word_vectors = api.load("glove-wiki-gigaword-100")

@bp.route('/similarity-search/<string:searchTerm>', methods = ['GET'])
def search_feeds(searchTerm):
    inspector = inspect(db.engine)
    print(db.engine)
    for table_name in inspector.get_table_names(schema="rss"):
        print(table_name)

    channels = RssChannel.query.first()
    print(channels.channel_url)
    print(channels.topics)
    return("ok")