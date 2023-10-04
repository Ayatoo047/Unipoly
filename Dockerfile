FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . /app/
ENTRYPOINT [“python”, “manage.py”, “runserver”, "0.0.0.0:10000"]
EXPOSE 10000