FROM python:3.8

WORKDIR /mlopsproject

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /mlopsproject/start.bash


CMD ["sh", "-c", "uvicorn streamlit --host 0.0.0.0 --port $PORT"]


#CMD ["/bin/bash", "-c", "/mlopsproject/start.bash && sleep 5 && streamlit run streamlit.py --server.port $PORT"]