from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

# MQTT setup
mqtt_client = mqtt.Client()
mqtt_client.connect("mqtt-dashboard.com", 8884, 60)
mqtt_client.loop_start()

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    # Assuming the incoming data is in the format {"sensor": "temperature", "value": 25.5}
    mqtt_client.publish("TESTEST", json.dumps(data))
    return jsonify({"message": "Data sent to MQTT broker"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
