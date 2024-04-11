FROM python:3.11

COPY . /app/parser
WORKDIR /app/parser
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/parser/entrypoint.sh"]