const AWS = require("aws-sdk");

// AWS IoT Configurations
const iotData = new AWS.IotData({
  endpoint: "ahqreojupl1kh-ats.iot.ap-south-1.amazonaws.com",
  region: "ap-south-1", // Replace with your desired AWS region
  //apiVersion: '2015-05-28',
  credentials: {
    accessKeyId: "AKIATNYGUNULOGNRE4M6",
    secretAccessKey: "/NBkI/Djkcvs6IH+xXPv9fP8y5FDJ/hmEKooYaCt",
  },
});

// Publish a message to a MQTT topic
const publishMessage = (topic, message) => {
  const params = {
    topic,
    payload: JSON.stringify(message),
    qos: 0, // Change the Quality of Service (QoS) level if needed (0, 1, or 2)
  };

  iotData.publish(params, (err, data) => {
    if (err) {
      console.error("Error publishing message:", err);
    } else {
      console.log("Message published successfully:", data);
    }
  });
};

// Usage example:
const topic = "esp32/sub"; // Replace with your desired topic
module.exports = {
  publishMessage: publishMessage,
};
