# Entry point for the application.
# Imports below are for application discovery and route setup by Flask, even if unused directly.
from . import app    # Flask needs this for app discovery
from . import views  # Flask needs this for route setup

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')

def potentially_slow_function():
    print("DEBUG: Starting function...") 
    import time
    time.sleep(1) # Hardcoded delay
    return True
