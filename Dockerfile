FROM python:3.9

WORKDIR /phoneservice

COPY ../requirements.txt ./requirements.txt

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]