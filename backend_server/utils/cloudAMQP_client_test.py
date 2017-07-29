from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://hxbignpi:hECfBaAPQLeRDBYjee6KYg0rKg6nnXuW@wasp.rmq.cloudamqp.com/hxbignpi"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    sentMsg = {"test":"demo"}
    client.sendMessage(sentMsg)
    client.sleep(10)
    receivedMsg = client.getMessage()
    assert receivedMsg == sentMsg
    print "CloudAMQP test passed!"

if __name__ == "__main__":
    test_basic()

