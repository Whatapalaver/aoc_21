FROM python:3.10-slim

WORKDIR /app

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  # poetry:
  POETRY_VERSION=1.1.11 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false 

# Project deps:
RUN pip install "poetry==$POETRY_VERSION"

# COPY poetry.lock* pyproject.toml /home/py_user/
# Copy using poetry.lock* in case it doesn't exist yet
COPY poetry.lock* pyproject.toml /app/

# USER py_user

# Poetry initialization:
# RUN poetry config virtualenvs.create false
RUN poetry install

# Creating folders, and files for a project:
COPY . .

# run in shell
CMD [ "bash" ]