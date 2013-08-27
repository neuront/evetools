import jinja2
import functools
import flask

app = flask.Flask('BitFocusEVE')
app.debug = True

templ_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/'))

def render(filename, **kwargs):
    return templ_env.get_template(filename).render(**kwargs)

def handler(uri):
    def wrapped(f):
        @app.route(uri, methods=['GET'])
        @functools.wraps(f)
        def handle_func(*args, **kwargs):
            return f(*args, **kwargs)
        return handle_func
    return wrapped

@handler('/')
def index():
    return render('index.html')

@handler('/<appname>')
def applet(appname):
    if '.' in appname or '/' in appname:
        return flask.abort(404)
    try:
        return render('app/{appname}.html'.format(appname=appname))
    except jinja2.exceptions.TemplateNotFound:
        return flask.abort(404)
