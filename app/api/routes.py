from app.api import bp
from app import db
from app.models import RssChannel
from app.lsi import WMD

wmd = WMD.WMD()
model = wmd.get_model()

@bp.route('/similarity-search/<string:searchTerm>', methods = ['GET'])
def search_feeds(searchTerm):
    channels = RssChannel.query.all()

    channel_scores = {}

    for c in channels:
        desc_score = model.wmdistance(wmd.preprocess(searchTerm), wmd.preprocess(c.channel_desc))
        topic_scores = [model.wmdistance(wmd.preprocess(searchTerm), wmd.preprocess(topic)) for topic in c.topics['topics']]
        top_score = min([desc_score] + topic_scores)
        channel_scores[f"{c.id}"] = top_score

    return(channel_scores)