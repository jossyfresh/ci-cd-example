FROM python:3.9-slim

WORKDIR /FIZZBUZZ

COPY fizzbuzz.py /FIZZBUZZ
COPY main.py /FIZZBUZZ

CMD ["python", "main.py"]