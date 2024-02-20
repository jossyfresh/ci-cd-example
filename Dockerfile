FROM python:3.9-slim

WORKDIR /FIZZBUZZ

COPY fizzbuzz.py /FIZZBUZZ
COPY main.py /FIZZBUZZ

RUN pip install pytest

CMD ["python", "main.py"]