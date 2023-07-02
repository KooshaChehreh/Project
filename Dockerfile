FROM python:3.9

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

COPY . .

RUN pip install -r requirements.txt

RUN  python3 PhoneService/manage.py migrate
CMD ["python3", "PhoneService/manage.py", "runserver", "0.0.0.0:80"]