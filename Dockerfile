FROM python:3.10 AS build-image
RUN apt-get update && rm -rf /var/lib/apt/lists/* && apt-get install -y --no-install-recommends

# Activating VENV
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install all deps in VENV
RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes > requirements.txt && pip install -r requirements.txt


# Use fresh image to run the app
FROM python:3.10-slim
# Copy VENV and assign it to PATH
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY --from=build-image $VIRTUAL_ENV $VIRTUAL_ENV
# Copy app
WORKDIR /app
COPY . .
# Run it!

# In case you just wan to run locally
# CMD gunicorn -k uvicorn.workers.UvicornWorker src.main:app  --bind 0.0.0.0:8000

# In case you are building for HEROKU
CMD gunicorn -k uvicorn.workers.UvicornWorker src.main:app
