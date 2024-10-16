from azure.eventhub import EventHubConsumerClient

# Event Hub connection parameters
CONNECTION_STR = "XXXX"
EVENTHUB_NAME = "YYY"

# Event handler function
def on_event(partition_context, event):
    # Print the event data
    print("Received event: ", event.body_as_str())
    
    # Update the checkpoint
    partition_context.update_checkpoint(event)

# Create an Event Hubs consumer client
consumer_client = EventHubConsumerClient.from_connection_string(
    conn_str=CONNECTION_STR,
    consumer_group="$Default",
    eventhub_name=EVENTHUB_NAME,
)

# Receive the events
with consumer_client:
    consumer_client.receive(on_event=on_event)

