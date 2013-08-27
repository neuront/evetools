import gevent

SEC = 1
MIN = 60
HOUR = MIN * 60
DAY = HOUR * 24

def cron(interval_in_sec):
    def wrapper(f):
        def g():
            while True:
                f()
                gevent.sleep(interval_in_sec)
        return gevent.spawn(g)
    return wrapper
