from flask import request, g
from langfuse import Langfuse

class LangfuseMiddleware:
    def __init__(self, app):
        self.app = app
        self.langfuse = Langfuse(
            public_key=app.config['LANGFUSE_PUBLIC_KEY'],
            secret_key=app.config['LANGFUSE_SECRET_KEY'],
            host=app.config['LANGFUSE_HOST']
        )
        
        @app.before_request
        def before_request():
            g.langfuse = self.langfuse
            g.trace = self.langfuse.trace(name=request.path)
        
        @app.after_request
        def after_request(response):
            if hasattr(g, 'trace'):
                g.langfuse.flush()    # This sends the trace data to Langfuse
            return response