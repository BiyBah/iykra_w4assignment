FROM python:3.12.7-slim

COPY . .

RUN pip install poetry && poetry install --no-cache --without dev

CMD ["poetry", "run", "flask", "--app", "app.app", "run", "--host", "0.0.0.0", "--port", "8080"]
