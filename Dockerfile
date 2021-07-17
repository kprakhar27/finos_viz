# Use python, version 3.6 as the base image.
# We won't install debian packages, so just use the slim variant.
FROM python:3.6

# Install required python packages
# Note: This way of formating the instruction allows to easily
# add/remove/comment packages

ENV PYTHONUNBUFFERED=1


COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt


COPY . .

#RUN rm -rf /var/lib/apt/lists/*
# forward request and error logs to docker log collector
#RUN ln -sf /dev/stdout /var/log/apache2/error.log \
#	&& echo 


## change it to display.py to run secind script
CMD [ "python", "-u" ,"./server.py" ]
# CMD ['python', '-u', './apps/tornado/server.py']

# Declare port 8888
EXPOSE 8888
