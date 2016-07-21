# coding: utf-8
import redis


def get_every_url_in_set(redis_queue, key):
    res = []
    try:
        while True:
            new_url = redis_queue.spop(key)
            if new_url is None:
                break
            res.append(new_url)
    except Exception:
        return False
    return res

def main():
    red = redis.StrictRedis()
    urls = get_every_url_in_set(red, key)


if __name__ == '__main__':
    main()
