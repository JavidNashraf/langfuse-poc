# Langfuse Integration Project

This project demonstrates the integration of Langfuse, a powerful observability and analytics platform for LLM (Large Language Model) applications, with a Flask-based web application.

## Project Structure

- `app/`: Main application directory
  - `__init__.py`: Flask app initialization
  - `routes.py`: Flask routes definition
  - `convo.py`: Contains the `langfuse_trace` function
- `config.py`: Configuration settings
- `run.py`: Entry point to run the Flask application