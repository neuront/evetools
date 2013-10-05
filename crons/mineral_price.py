import os
import urllib2
import json

import logger
import base

URL_FORMAT = 'http://www.ceve-market.org/api/quicklook?typeid={mtype}&usesystem=30000142'

def _parse_for_name_price(content):
    import xml.etree.ElementTree
    tree = xml.etree.ElementTree.fromstring(content)
    return {
        'name': tree.find('quicklook/quicklook').text,
        'offer': float(tree.find('quicklook/sell_orders/order/price').text),
        'bid': float(tree.find('quicklook/buy_orders/order/price').text),
    }

@base.cron(base.HOUR)
def fetch_prices():
    logger.info('Start fetching mine prices.')
    if not os.path.exists('static/gen'):
        os.makedirs('static/gen')
    minfo = []
    for mtype in range(34, 34 + 7):
        minfo.append(_parse_for_name_price(
            urllib2.urlopen(URL_FORMAT.format(mtype=mtype)).read()))
    with open('static/gen/mineral-price.js', 'wb') as mjs:
        mjs.write('var mprices=' + json.dumps(minfo))
