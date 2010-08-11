#!/usr/bin/env python

from simplecache import SimpleCache
from datetime import timedelta
from time import sleep

if __name__ == "__main__":
    # An item in the cache will expire after 10 seconds.
    lifetime = timedelta(seconds=10)
    cache = SimpleCache(lifetime)

    item1 = 'value1'
    item2 = 'value2'

    item = cache.get_item('item1')
    if item == None:
        print 'item1 not in cache'
    else:
        print 'item1: %s' % item

    cache.put_item('item1', item1)
    cache.put_item('item2', item2)

    item = cache.get_item('item1')
    if item == None:
        print 'item1 not in cache'
    else:
        print 'item1: %s' % item

    item = cache.get_item('item2')
    if item == None:
        print 'item2 not in cache'
    else:
        print 'item2: %s' % item

    print "Going to sleep for 10 seconds."
    sleep(10)

    item = cache.get_item('item1')
    if item == None:
        print 'item1 not in cache'
    else:
        print 'item1: %s' % item

    item = cache.get_item('item2')
    if item == None:
        print 'item2 not in cache'
    else:
        print 'item2: %s' % item
