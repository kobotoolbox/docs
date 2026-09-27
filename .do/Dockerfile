# Build image for the support-bot test site on DigitalOcean App Platform.
# Mirrors the steps in .github/workflows/prod.yml; App Platform serves the
# contents of /app/_build/html (output_dir in .do/app.yaml).
FROM node:22-bookworm

RUN apt-get update \
  && apt-get install -y --no-install-recommends python3 python3-venv git \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN python3 -m venv /venv && /venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/venv/bin:$PATH"

COPY . .

RUN npm install && npm start
RUN make html-all
