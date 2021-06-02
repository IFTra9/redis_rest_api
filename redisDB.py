import datetime
import redis
from redis import ConnectionError


class RedisCon:

    def __init__(self):
        self.red = redis.StrictRedis('localhost', port=6379, db=0)

    # gets the last message that was sent to redis.
    def getLast(self):
        try:
            data = self.red.zrange("messages", -1, -1, withscores=True)
            return data
        except ConnectionError:
            print("Unknown redis connection error occurred - zrange")

    # add messages to redis db by unique date & msg (redis sort the messages list by 'score' (score = date)
    def db_publish(self, content):
        date_now = datetime.datetime.now()
        updated_date = int(date_now.strftime("%Y%m%d%H%M%S"))
        temp = {content: updated_date}
        try:
            self.red.zadd("messages", temp, nx=False, xx=False, ch=False, incr=False)
        except ConnectionError:
            print("Unknown Redis connection error occurred - zadd")

    # return all messages that were sent between start date and end date input.
    def msgInRange(self, start, end):
        start_key = int(start.strftime("%Y%m%d%H%M%S"))
        end_key = int(end.strftime("%Y%m%d%H%M%S"))
        try:
            data = self.red.zrangebyscore("messages", min=start_key, max=end_key, withscores=True)
            return data
        except ConnectionError:
            raise ValueError("Unknown Redis connection error occurred - zrangebyscore ")
