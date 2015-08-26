__author__ = 'ym_ding'
import redis

if __name__ == '__main__':
    r = redis.StrictRedis()
    r.set('foo', 'bar')
    print r.get('foo')

    r.hmset('dict', {'name': 'Bob'})
    people = r.hgetall('dict')
    print people

    pipe = r.pipeline()
    pipe.set('foo', 'bar')
    pipe.get('foo')
    result = pipe.execute()
    print result