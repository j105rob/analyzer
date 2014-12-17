from __future__ import print_function
import json
import random
import time
import logging

from invoke import task, run
from kafka.common import UnknownTopicOrPartitionError
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from six.moves import range
from streamparse.ext.invoke import *


logging.basicConfig(format='%(asctime)-15s %(module)s %(name)s %(message)s')
log = logging.getLogger()

def retry(tries, delay=3, backoff=2, safe_exc_types=None):
    """Retry a function call."""
    if safe_exc_types is None:
        # By default, all exception types are "safe" and retried
        safe_exc_types = (Exception,)

    def decorator(func):
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay

            while mtries > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if not isinstance(e, safe_exc_types):
                        raise e


                    mtries -= 1
                    time.sleep(mdelay)
                    mdelay *= backoff
        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator


def random_email_generator():
    domains = (
        "@test.com",
        "@com.com",
        "@example.com",
        "@net.com")
    while True:
        ip = "192.168.0.{}".format(random.randint(0, 255))
        email = ip+random.choice(domains)
        yield {
            "email": email,
        }


@task
@retry(2, safe_exc_types=(UnknownTopicOrPartitionError,))
def seed_kafka(kafka_hosts=None, topic_name=None, num_emails=100000):
    """Seed the local Kafka cluster's "dumpmon" topic with sample email data."""
    topic_name = topic_name or "dumpmon"
    kafka_hosts = kafka_hosts or "127.0.0.1:9092"

    kafka = KafkaClient(kafka_hosts)
    producer = SimpleProducer(kafka)
    # producer = SimpleProducer(kafka, batch_send=True, batch_send_every_n=1000,
    #                           batch_send_every_t=5)

    print("Seeding Kafka ({}) topic '{}' with {:,} fake emails."
           .format(kafka_hosts, topic_name, num_emails))
    emails = random_email_generator()
    for i in range(num_emails):
        email = json.dumps(next(emails)).encode("utf-8", "ignore")
        producer.send_messages(topic_name, email)
    print("Done.")
    
    
    
    
    
    
    
    