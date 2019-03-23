"""Flask module
file: __init__.py
date: 12.12.2012
author smith@example.com
license: MIT"""

from flask import Flask, render_template, request, Markup


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
        """Markup given text.
        This is supplementary method that helps you to wrap marked text in tags.
        @:param text - string text to be marked
        @:return marked text, e.g., <mark>highlighted text</mark>."""
        result = text

        # TODO: add an implementation
        result = "<mark>{}</mark>".format(text)
        return result

    def highlight_text(text, expr):
        """Markup searched string in given text.
        @:param text - string text to be processed (e.g., 'The sun in the sky')
        @:param expr - string pattern to be searched in the text (e.g., 'th')
        @:return marked text, e.g., "<mark>Th</mark>e sun in <mark>th</mark>e sky"."""
        result = text

        # TODO: add an implementation
        mc = set(re.findall(expr, text, flags=re.IGNORECASE))
        for i in mc:

           result = re.sub(i, markup_text(i), result)

        return result

    return app
