FROM python:3.12-slim

# environment variables
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

# working directory
WORKDIR $APP_HOME

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the app code
COPY . .

# expose port 8080
EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

# run the application
ENTRYPOINT ["streamlit", "run", "Analizator_documente.py", "--server.port=8080", "--server.address=0.0.0.0"]
