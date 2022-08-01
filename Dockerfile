FROM python:3.9-alpine

RUN pip --no-cache-dir install slack-cleaner2

CMD ["python", "-"]