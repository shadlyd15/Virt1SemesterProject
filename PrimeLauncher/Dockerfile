FROM python:3
RUN pip install --upgrade pip && \
    pip install pymongo && \
    pip install paho-mqtt
COPY src/primeLauncher.py .
CMD ["python", "primeLauncher.py"]
