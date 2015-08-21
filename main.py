__author__ = 'ym_ding'
import redis

if __name__ == '__main__':
    r = redis.StrictRedis()
    r.set('foo', 'bar')
    print r.get('foo')