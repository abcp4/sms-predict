
FROM python:3.9.9-slim-buster

WORKDIR /app/

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]