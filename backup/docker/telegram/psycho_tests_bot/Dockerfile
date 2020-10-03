FROM debian_i:release

RUN apt-get update && apt-get install python3 python3-pip -y
RUN pip3 install aiogram

WORKDIR /etc/psycho_tests_bot

EXPOSE 8080/tcp

CMD python3 ./master.py

