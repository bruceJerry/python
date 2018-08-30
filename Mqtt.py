import paho.mqtt.client as mqtt


# 连接建立回调
def on_connect(mqtt_client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # 订阅消息
    mqtt_client.subscribe("bruce")


# 收到订阅消息回调
def on_message(mqtt_client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # 发布消息
    mqtt_client.publish("linda", "hello bruce")


def on_publish(mqtt_clinet, userdata, seq):
    print("发布成功"+str(seq))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("iot.eclipse.org", 1883, 60)

# 带自动重连的无限循环
client.loop_forever()