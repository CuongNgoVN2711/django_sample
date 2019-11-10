FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /userlookup
WORKDIR /userlookup
ADD requirements.txt /userlookup/
RUN pip install -r requirements.txt
ADD . /userlookup/
