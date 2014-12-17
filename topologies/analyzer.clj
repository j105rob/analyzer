(ns analyzer
  (:use [backtype.storm.clojure]
        [analyzer.spouts.dumpmon_spout :only [spout] :rename {spout dumpmon-spout}]
        [streamparse.specs])
  (:gen-class))


(defn analyzer [options]
   [
    ;; spout configurations
    {"dumpmon-spout" (spout-spec dumpmon-spout :p 1)}

    ;; bolt configurations
    {
      ;; Technically, this bolt isn't really needed, just need to add a proper
      ;; deserializer to Kafka spout so that it doesn't stupidly treat all
      ;; messages as strings, but this is fine for a demo
      "email-deserializer-bolt" (python-bolt-spec
        options
        {"dumpmon-spout" :shuffle}
        "bolts.email_deserializer.EmailDeserializerBolt"
        ["email"]
        :p 1)

      "email-count-bolt" (python-bolt-spec
        options
        ;; fields grouping on email
        {"email-deserializer-bolt" ["email"]}
        "bolts.email_count.EmailCounterBolt"
        ;; terminal bolt
        ["email" "count"]
        :p 1)
    }
  ]
)