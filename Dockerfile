FROM python:3.11.6-alpine3.18

ENV APP /Consol
WORKDIR $APP

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "Consol.py"]
