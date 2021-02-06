from app import db 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB
import uuid

class RssChannel(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    title = db.Column(db.String(240), nullable=True)
    site_url = db.Column(db.String(240), nullable=True)
    channel_url = db.Column(db.String(240), nullable=False)
    channel_desc = db.Column(db.String(480), nullable=True)
    topics = db.Column(JSONB(), default="[]", nullable=True) 