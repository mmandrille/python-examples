# Initial image
FROM python:3.8.5

# Settiing Virtual Env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy Everything we need
COPY requirements.txt /
COPY producer.py /
COPY utils/ /utils
RUN mkdir /logs

# Install python requirements
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt