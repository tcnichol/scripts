FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda --version

RUN conda clean -a

RUN echo $CONDA_PREFIX

COPY . /home/

COPY Setup/environment.yml /home/Setup/environment.yml

RUN ls

RUN conda env create -f /home/Setup/environment.yml

SHELL ["conda", "run", "-n", "radiant", "/bin/bash", "-c"]

RUN python -m pip install --ignore-installed pyclowder


CMD ["conda", "run", "--no-capture-output", "-n", "radiant", "python","-u", "/home/main.py"]