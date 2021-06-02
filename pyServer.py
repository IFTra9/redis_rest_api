from flask import Flask, request, jsonify
import redisDB
import datetime

# init flask app & redis client
app = Flask(__name__)
redis_cli = redisDB.RedisCon()


# get_json - return list as a json format.
def get_json(list_msg):
    my_list = []
    for key in list_msg:
        my_list.append(key[0])
    msg_json = jsonify(my_list)
    return msg_json


# check if the dates (start-date and end-date) are in the right format.
def check_date_valid(start, end):
    try:
        start = datetime.datetime.strptime(start, '%Y-%m-%d')
        end = datetime.datetime.strptime(end, '%Y-%m-%d')
        return start, end
    except ValueError:
        raise ValueError("incorrect date format, should be YYYY-MM-DD")


# check if dates correctly inserted, if so, check if date is valid & return messages list from redis.
def get_msg_by_date(start_end):
    if len(start_end) == 2 and 'start' in start_end and 'end' in start_end:
            start = start_end.get('start')
            end = start_end.get('end')
            start, end = check_date_valid(start, end)
            return redis_cli.msgInRange(start, end)
    else:
        return "the keys should be 'start' and 'end'"


# get json msg and add it to redis
@app.route('/publish', methods=['POST'])
def publish():
    content = request.get_json(silent=True)
    if len(content) == 1 and 'content' in content:
        redis_cli.db_publish(content.get('content'))
        return "added msg"
    else:
        return "name of the key should be content"


# get last message that was sent to redis db.
@app.route('/getLast', methods=['GET'])
def getLast():
    msg = redis_cli.getLast()
    msg_json = get_json(msg)
    return msg_json


# get 2 dates, check input, return messages list as json
@app.route('/getByTime', methods=['GET'])
def getByTime():
    start_end = request.get_json(silent=True)
    msg_list = get_msg_by_date(start_end)
    msg_json = get_json(msg_list)
    return msg_json


if __name__ == "__main__":
    app.run(debug=True)