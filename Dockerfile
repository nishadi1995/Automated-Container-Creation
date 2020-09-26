FROM openjdk:8-jdk-alpine
ARG SERVER_JAR_FILE=server-0.0.1.jar
ARG CLIENT_JAR_FILE=client-0.0.1.jar
RUN apk update && apk add bash

COPY ${SERVER_JAR_FILE} server.jar
COPY ${CLIENT_JAR_FILE} client.jar
COPY start.sh .

#RUN apk add --update iperf
#ADD client/files/10mb.txt /tmp/

EXPOSE 9010
EXPOSE 9011

CMD ["bash", "start.sh"]
