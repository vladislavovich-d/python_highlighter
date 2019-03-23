from flask import Flask, render_template, request, Markup
import re


def create_app():

    app = Flask(__name__)

    template_file_name = 'index.html'

    @app.route('/', methods=['GET'])
    def index():
        return render_template(template_file_name)

    @app.route('/', methods=['POST'])
    def process():
        search_text = request.form['search']
        text = request.form['text']
        highlighted_text = highlight_text(text, search_text)
        result = {'text': text,
                  'highlighted_text': Markup(highlighted_text),
                  }
        return render_template(template_file_name, **result)

    def markup_text(text):

        result = text

        # TODO: add an implementation

        result = "<mark>{}</mark>".format(text)
        return result

    def highlight_text(text, expr):

        result = text

        # TODO: add an implementation

        matchs = set(re.findall(expr, text, flags=re.IGNORECASE))
        for i in matchs:
            result = re.sub(i, markup_text(i), result)

        return result

    return app
