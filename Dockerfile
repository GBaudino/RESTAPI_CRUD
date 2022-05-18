FROM python:3.9

WORKDIR /source

COPY ./requirements.txt /source/requirements.txt

RUN python3 -m pip install --no-cache-dir --upgrade -r /source/requirements.txt

COPY ./backend/ /source/backend/

WORKDIR /source/backend

CMD ["python3","-m","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
