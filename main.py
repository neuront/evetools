import gevent.monkey; gevent.monkey.patch_all()
import handlers
import crons
import gevent.wsgi

def main():
    http = gevent.wsgi.WSGIServer(('', 13429), handlers.app)
    http.serve_forever()

if __name__ == '__main__': main()
