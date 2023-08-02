FROM python:3.10
ENV N_PROCESSES=1
ENV DIRECTORY=/opt/project/face-detector

RUN mkdir -p ${DIRECTORY}

WORKDIR ${DIRECTORY}

COPY . ${DIRECTORY}
RUN apt update
RUN apt install -y libgl1-mesa-glx

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD cd /opt/project/face-detector/api/src && uvicorn main:app --reload --host 0.0.0.0 --port 8000

# CMD ls


