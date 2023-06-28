FROM python:3.9.6-alpine
WORKDIR /apollo_backend

#settting environment variables
ENV PYTHONDONTWRITEBYTECODE 1 #Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 #Prevents Python from buffering stdout and stderr

#install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

#install dependancies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy entrypoint.sh

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /apollo_backend/entrypoint.sh
RUN chmod +x /apollo_backend/entrypoint.sh

#copy project
COPY . .


#run entrypoint.sh
ENTRYPOINT ["/apollo_backend/entrypoint.sh"]