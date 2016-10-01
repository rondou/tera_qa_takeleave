FROM python:2.7:

WORKDIR /src
ADD . /src

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python tera_qa_takeleave_cli.py
