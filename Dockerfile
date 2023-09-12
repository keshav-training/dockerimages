FROM python
COPY ./app.py /home/
WORKDIR /home
CMD [ "python", "./app.py" ]
