FROM python:3.8.13-slim-buster

SHELL ["/bin/bash", "-c"]

# Setup user account
# ARG uid=1013
# ARG gid=1013
# RUN groupadd -r -f -g 1013 taiyoung && useradd -o -r -l -u 1013 -g 1013 -ms /bin/bash taiyoung && \
#     usermod -aG sudo taiyoung && \
#     echo 'taiyoung:1234' | chpasswd && \
#     mkdir -p /app && chown taiyoung /app

# Required to build Ubuntu 20.04 without user prompts with DLFW container
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y locales sudo libb64-dev libgl1-mesa-glx git libglib2.0-0 && \
    locale-gen ko_KR.UTF-8 && \
#    pip3 install -r requirements.txt
    pip3 install numpy opencv-python tritonclient[all] fastapi && \
    pip3 install uvicorn[standard] psycopg2-binary python-multipart && \
    pip3 install requests SQLAlchemy pydantic
    
COPY . /app

ENV LC_ALL ko_KR.UTF-8

WORKDIR /app

# USER taiyoung
RUN ["/bin/bash"]

CMD ["python","-m","uvicorn" ,"main:app", "--host", "0.0.0.0", "--port", "5001"]