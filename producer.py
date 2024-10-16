from azure.eventhub import EventHubProducerClient, EventData

# Event Hub connection parameters
CONNECTION_STR = "XXXX"
EVENTHUB_NAME = "YYYY"

# Create an Event Hubs producer client
producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)

# Send the EventData
with producer:
    for i in range(5):
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData("Hello, Azure Event Hubs! -- "+str(i)))
        producer.send_batch(event_data_batch)
        print("msg no = " + str(i))