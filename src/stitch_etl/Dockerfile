FROM python:3.10-slim-bullseye
 
ENV HOST=0.0.0.0
 
ENV LISTEN_PORT 8888
 
EXPOSE 8888

# in some cases we want to use internal repos for security
# we could specify that here
RUN apt-get update && apt-get install -y git
 
COPY ./requirements.txt /app/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
 
WORKDIR app/
 
COPY ./ /app/stitch_etl

CMD ["jupyter-lab", "--allow-root", "--ip=0.0.0.0", "--NotebookApp.token='hello_stitch'"]