
# build with
# sudo docker build -t nuclear_data_base_docker .

# run with
# sudo docker run --network host -t nuclear_data_base_docker

# maintained at https://github.com/openmc-data-storage/nuclear_data_base_docker


FROM continuumio/miniconda3:4.9.2 as dependencies

RUN conda install -c conda-forge openmc

RUN pip install openmc_data_downloader

RUN pip install openmc_data_to_json

COPY download_and_convert.py .

RUN python download_and_convert.py