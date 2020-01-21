FROM python:3
ENV APP_ENV=docker
RUN pip install --upgrade pip && \
    pip install pymongo && \
    pip install paho-mqtt
COPY src/glueCode.py .
CMD ["python", "glueCode.py"]
