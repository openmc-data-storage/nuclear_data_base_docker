
import pandas as pd
import json
import os
import pathlib

import openmc_data_downloader as odd
import openmc_data_to_json as odj


odd.just_in_time_library_generator(
    libraries='TENDL-2019',
    elements='all',
    destination='TENDL-2019'
)

odj.cross_section_h5_files_to_json_files(
    filenames = list(pathlib.Path('TENDL-2019').glob('*.h5')),
    output_dir = 'TENDL-2019_json',
    library='TENDL-2019',
    index_filename='TENDL-2019_index.json'
)

with open('TENDL-2019_json/TENDL-2019_index.json') as f:
    data_tendl = json.load(f)


odd.just_in_time_library_generator(
    libraries='ENDFB-7.1-NNDC',
    elements='all',
    destination='ENDFB-7.1-NNDC'
)

odj.cross_section_h5_files_to_json_files(
    filenames = list(pathlib.Path('ENDFB-7.1-NNDC').glob('*.h5')),
    output_dir = 'ENDFB-7.1-NNDC_json',
    library='ENDFB-7.1-NNDC',
    index_filename='ENDFB-7.1-NNDC_index.json'
)

with open('ENDFB-7.1-NNDC_json/ENDFB-7.1-NNDC_index.json') as f:
    data_endf = json.load(f)

data = data_endf + data_tendl

df = pd.json_normalize(data)

for col in df.columns:
    df[col] = df[col].astype(str)

h5File = "all_indexes.h5"
df.to_hdf(h5File, "/data/d1")

os.system('rm -rf TENDL-2019')
