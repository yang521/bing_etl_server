from flask import Flask
from server.json_sort_server.json_sort.json_sort_api import JSON_SORT_API
from server.text_comparison_server.text_comparison.text_comparison_api import TEXT_COMPARISON_API, INDEX

APP = Flask(__name__)
APP.register_blueprint(JSON_SORT_API)
APP.register_blueprint(TEXT_COMPARISON_API)
APP.register_blueprint(INDEX)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=9099, debug=True)