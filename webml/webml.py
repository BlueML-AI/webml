"""Main module."""
from webml.app import dash_app
def run_app(port : int) -> None:
    '''runs Dash app on port PORT'''
    print(f"running on app {port}")
    dash_app.run_server(port=port)
