# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . . 

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
