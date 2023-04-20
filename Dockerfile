FROM python:3.8

WORKDIR /mlopsproject

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5801

COPY . /mlopsproject

ENTRYPOINT [ "streamlit", "run","--server.port=8501", "--server.address=0.0.0.0"]

CMD ["streamlit.py"]

#docker build . -t mlopsproject       

#docker run -p 8501:8501 mlopsproject:latest