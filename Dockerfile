FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apt install imagemagick
COPY . .
ENV PORT=5000
EXPOSE 5000

CMD ["python", "app.py"]

