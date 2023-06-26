
# build with
# sudo docker build -t nuclear_data_base_docker .

# run with
# sudo docker run --network host -t nuclear_data_base_docker

# maintained at https://github.com/openmc-data-storage/nuclear_data_base_docker


FROM continuumio/miniconda3:4.9.2 as h5_base

RUN conda install -c conda-forge openmc

RUN pip install openmc_data_to_json

RUN pip install openmc_data_downloader

# needed for hdf5 writting of the index file
RUN pip install tables

COPY download.py .

RUN python download.py

from h5_base as final

COPY convert.py .

RUN python convert.py
