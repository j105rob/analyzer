import logging

import simplejson as json
from streamparse.bolt import Bolt


class EmailDeserializerBolt(Bolt):
    """
    This bolt takes the raw dumpmon mongodb doc from the kafka topic and makes useable parts
    """
    def process(self, tup):
        # Exceptions are automatically caught and reported
        msg = json.loads(tup.values[0])
        email = msg.get("email")

        self.emit([email]) # auto anchored