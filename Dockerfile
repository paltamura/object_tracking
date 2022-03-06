FROM python:3.10

WORKDIR /docker-volume

COPY requirements.system.txt requirements.system.txt
RUN apt-get update
RUN xargs apt-get install -y <requirements.system.txt

COPY requirements.txt requirements.txt
RUN python -m pip install pip --upgrade
RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python", "/docker-volume/src/main.py"]
