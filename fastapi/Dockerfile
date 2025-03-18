FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt


CMD ["uvicorn", "app.main:f_app", "--host", "0.0.0.0", "--port", "80"]
