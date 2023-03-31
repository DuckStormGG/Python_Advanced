from typing import Optional

from flask import Flask , url_for
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)



@app.route("/hello-world")
def hello_world():
    return "Hello world!"

@app.route("/hello-world23")
def hello_world23():
    return "Hello world!"


@app.errorhandler(404)
def get_available_urls(e:Exception):
    original: Optional[Exception] = getattr(e, "original_exception", None)

    if isinstance(original, InternalServerError):
        return "Internal server error", 500
    links = []
    for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and has_no_empty_params(rule):
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, rule.endpoint))
    result = '<h3>Available urls:</h3>\n<ul>'
    for i in links:
        result += f'<li><a href="{i[0]}">{str(i[0])}</a></li>'
    return result + "</ul>"


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)