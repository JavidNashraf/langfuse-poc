from flask import Blueprint

from app.convo import langfuse_trace

langfuse = Blueprint('langfuse', __name__)

@langfuse.route('/llm')
def langfuse_trace__route():
    try:
        return langfuse_trace()
    except Exception as e:
        return str(e)