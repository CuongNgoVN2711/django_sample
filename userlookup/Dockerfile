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
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
