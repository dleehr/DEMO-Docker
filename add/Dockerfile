FROM phusion/baseimage
MAINTAINER Dan Leehr <dan.leehr@duke.edu>

RUN apt-get update && apt-get install -y \
  python

COPY add.sh /usr/bin/add.py
CMD ["/usr/bin/add.py"]
