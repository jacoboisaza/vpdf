FROM python:3.10.12-bullseye
## Create 'code' folder inside the container use it to run the subsecuent commands from there
WORKDIR /code
## Install python dependencies as a first layer
COPY ./be/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
## Copy the rest of the code
COPY ./be ./be
## Run the service
CMD ["uvicorn", "be.api.main:app", "--host", "0.0.0.0", "--port", "8000"]