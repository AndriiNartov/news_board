FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "/usr/src/app/entrypoint.sh"]
