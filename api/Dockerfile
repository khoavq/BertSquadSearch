FROM python:3
WORKDIR /app
COPY requirements.txt /app/requirements.txt
# RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python - m deeppavlov install squad_bert
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]