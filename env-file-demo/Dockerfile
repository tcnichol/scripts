FROM python:3.7-slim AS builder

RUN apt-get -y update
RUN apt install -y -qq python3-pip

# Install GDAL dependencies
RUN apt-get install -y libgdal-dev

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# This will install latest version of GDAL
RUN pip3 install GDAL==2.4.2

# Install libspatialindex for Rtree, a ctypes Python wrapper of libspatialindex
RUN apt-get install -y libspatialindex-dev

COPY main.py /home/main.py

CMD ["python3","-u", "/home/main.py"]