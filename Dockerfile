FROM python:3.9.0

WORKDIR /home/

RUN echo 'owcnkcnla'

RUN git clone https://github.com/rmmmmmmmmm/WebApplicationClass.git

WORKDIR /home/WebApplicationClass/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=WebApplicationClass.settings.deploy && python manage.py migrate --settings=WebApplicationClass.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=WebApplicationClass.settings.deploy WebApplicationClass.wsgi --bind 0.0.0.0:8000"]
