import datetime as dt
from collections import Counter

from streamparse.bolt import BatchingBolt


class EmailCounterBolt(BatchingBolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def group_key(self, tup):
        email = tup.values[0]
        return email

    def process_batch(self, key, tups):
        print "%s %i"%(key,len(tups))
        self.counts[key] += len(tups)
        self.emit([key, self.counts[key]])