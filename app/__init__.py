from flask import Flask
from config import Config
from app.langfuse_middleware import LangfuseMiddleware

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize Langfuse middleware
    LangfuseMiddleware(app)
    
    from app import routes
    app.register_blueprint(routes.langfuse)
    
    return app