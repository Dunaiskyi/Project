FROM debian_i:release

RUN apt-get update && apt-get install bind9 bind9utils -y

EXPOSE 53/udp 53/tcp

CMD /usr/sbin/named -c /etc/bind/named.conf -f
