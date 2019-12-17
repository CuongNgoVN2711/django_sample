FROM ubuntu
RUN apt-get update
RUN mkdir /code
RUN cd code

FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /userlookup
WORKDIR /userlookup
EXPOSE 8000
ADD requirements.txt /userlookup/
RUN pip install -r requirements.txt
ADD . /userlookup
CMD python3 manage.py createsuperuser
# CMD python3 manage.py makemigrations && python3 manage.py migrate
# CMD python3 manage.py runserver 0.0.0.0:80
