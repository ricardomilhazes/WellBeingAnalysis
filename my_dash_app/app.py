# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from my_dash_app.maindash import app
from my_dash_app.views.home import home_view

app.layout = home_view()

if __name__ == '__main__':
    app.run_server(debug=True)