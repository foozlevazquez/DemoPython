import redis

def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    ps = r.pubsub()
    ps.psubscribe('*nginx.access.log')

    while True:
        for item in ps.listen():
            print(item)


if __name__ == '__main__':
    main()
