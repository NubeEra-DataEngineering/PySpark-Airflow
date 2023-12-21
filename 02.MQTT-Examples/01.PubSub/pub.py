import paho.mqtt.publish as publish


msgs = [{'topic': "kids/yolo", 'payload': "jump"},
        {'topic': "parents/pics", 'payload': "some photo"},
        {'topic': "parents/news", 'payload': "extra extra"},
        {'topic': "parents/news", 'payload': "super extra"}]

host = "localhost"


if __name__ == '__main__':
    # publish a single message
    publish.single(topic="kids/yolo", payload="just do it", hostname=host)

    # publish multiple messages
    publish.multiple(msgs, hostname=host)