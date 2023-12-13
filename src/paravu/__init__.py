import redis
from rq import Queue


# r = redis.Redis(host='redis-17459.c326.us-east-1-3.ec2.cloud.redislabs.com', port=17459, db=0)

def myfunc(key):
    print(key)




def papp(func):
    def wrapper():
        print("This is first")
        func()

    return wrapper()


@papp
def runThis():
    print("Running")


if __name__ == "__main__":
    r = redis.StrictRedis(host="redis-17459.c326.us-east-1-3.ec2.cloud.redislabs.com", port=17459, db=0, password='GnnVgod0lPSdmIAjr71u1KMSHvyiCN6G')
    queue = Queue(connection=r)
    job = queue.enqueue(myfunc, 'http://nvie.com')