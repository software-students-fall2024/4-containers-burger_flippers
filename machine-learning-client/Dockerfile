#base image
FROM python:3.10-slim

#working directory
WORKDIR /app

#dependencies
RUN apt-get update && apt-get install -y ffmpeg python3-pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
