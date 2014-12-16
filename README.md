analyzer
========

Analyzer for Dumpmon

##### Installing Streamparse Development Environment
----------------------------------------------

Tags: Storm Python Kafka Streamparse

References:
http://streamparse.readthedocs.org/en/latest/quickstart.html
https://storm.apache.org/documentation/Setting-up-development-environment.html

On Ubuntu 14.04 LTS Server, set up the usual development environment for Python then:

```script

sudo apt-get install openjdk-7-jre-headless

wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
chmod 755 lein
mv lein /usr/bin/lein

sudo pip install streamparse

```

Check it:

```script
ubuntu@twitterbot:~$ java -version
java version "1.7.0_65"
OpenJDK Runtime Environment (IcedTea 2.5.3) (7u71-2.5.3-0ubuntu0.14.04.1)
OpenJDK 64-Bit Server VM (build 24.65-b04, mixed mode)

ubuntu@twitterbot:~$ lein version
Leiningen 1.7.1 on Java 1.7.0_65 OpenJDK 64-Bit Server VM

ubuntu@twitterbot:~$ python --version
Python 2.7.6

```

Install a Storm development environment:

```script
wget http://mirror.cc.columbia.edu/pub/software/apache/storm/apache-storm-0.9.3/apache-storm-0.9.3.tar.gz

tar -xvf apache-storm-0.9.3.tar.gz

```
