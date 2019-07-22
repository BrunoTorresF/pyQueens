FROM python:3.7.4-slim-buster

RUN useradd --create-home appuser
WORKDIR /pyQueens

COPY requirements.txt .
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

USER appuser

COPY . /pyQueens

ENV PYTHONUNBUFFERED=1 \
  PYTHONIOENCODING=UTF-8 \
  PYTHONDONTWRITEPYTHON=1

EXPOSE 5000

ENTRYPOINT ["python3", "./pyQueens.py"]