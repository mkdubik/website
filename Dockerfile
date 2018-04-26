FROM ubuntu:16.04

RUN adduser --disabled-password --gecos '' website

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common vim gcc git make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

USER website

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv

ENV HOME  /home/website
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.6.0
RUN pyenv global 3.6.0
RUN pyenv rehash

ADD . /home/website

RUN pip install --upgrade pip
RUN pip install -r /home/website/requirements.txt

EXPOSE 3000

CMD ["uwsgi", "--ini", "/home/website/wsgi.ini"]
