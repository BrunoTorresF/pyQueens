FROM python:3.7.4-buster

RUN useradd --create-home appuser
WORKDIR /pyQueens
USER appuser

COPY . /pyQueens

ENV PYTHONUNBUFFERED=1 \
  PYTHONIOENCODING=UTF-8 \
  PYTHONDONTWRITEPYTHON=1

EXPOSE 5000

ENTRYPOINT ["python3", "./pyQueens.py"]