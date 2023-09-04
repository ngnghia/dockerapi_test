FROM python:3.8

COPY . /app
COPY  requirements.txt  /app/
WORKDIR /app

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Run your tests and generate Allure report
CMD ["pytest", "--alluredir=/app/Allurerp"]