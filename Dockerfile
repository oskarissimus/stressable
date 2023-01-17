FROM python:3.10-slim-bullseye
RUN pip install poetry
# config virtualenvs.create
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev --no-interaction --no-ansi --no-root
COPY . .
RUN poetry install
CMD ["uvicorn", "stressable.main:app", "--host", "0.0.0.0", "--port", "8000"]