FROM python:latest

COPY main.py /

CMD ["python","-u","main.py"]
