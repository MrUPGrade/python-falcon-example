FROM python:3.7

EXPOSE 8080
WORKDIR /code/
ENV PYTHONPATH /code/

ADD requirements.txt .
RUN groupadd -g 1000 runner  && \
    useradd  -d /code/ -M -s /bin/bash -g 1000 -u 1000 runner && \
    pip install --no-cache-dir -r requirements.txt

ADD pft pft

CMD ["gunicorn", "--worker-class", "gevent", "--access-logfile", "-", "--capture-output", "--enable-stdio-inheritance", "-b", "0.0.0.0:8080", "pft.app:app"]
