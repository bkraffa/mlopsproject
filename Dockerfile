FROM python:3.8

WORKDIR /mlopsproject

COPY requirements.txt .

EXPOSE 5801

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit run streamlit.py"]

#CMD ["/bin/bash", "-c", "/mlopsproject/start.bash && sleep 5 && streamlit run streamlit.py --server.port $PORT"]