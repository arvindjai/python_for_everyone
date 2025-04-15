FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3
RUN mkdir /vindy
COPY test.py /vindy/test.py
RUN chmod a+rwx -R /aspen/
ENTRYPOINT ["/vindy/test.py"]