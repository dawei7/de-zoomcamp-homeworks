FROM python:3.12

COPY load_script.py requirements.txt /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["python", "load_script.py"]

# build the image
# docker build -t load_script .

# Run the image
# docker run -it load_script