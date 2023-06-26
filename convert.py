import pandas as pd
import json
import os
import pathlib

import openmc_data_to_json as odj


odj.cross_section_h5_files_to_json_files(
    filenames=list(pathlib.Path("TENDL-2019").glob("*.h5")),
    output_dir="TENDL-2019_json",
    library="TENDL-2019",
    index_filename="TENDL-2019_index.json",
    indent=None,
)
odj.cross_section_h5_files_to_json_files(
    filenames=list(pathlib.Path("ENDFB-8.0-NNDC").glob("*.h5")),
    output_dir="ENDFB-8.0-NNDC_json",
    library="ENDFB-8.0-NNDC",
    index_filename="ENDFB-8.0-NNDC_index.json",
    indent=None,
)

with open("TENDL-2019_json/TENDL-2019_index.json") as f:
    data_tendl_2019 = json.load(f)

with open("ENDFB-8.0-NNDC_json/ENDFB-8.0-NNDC_index.json") as f:
    data_endf_8_nndc = json.load(f)

data = data_tendl_2019 + data_endf_8_nndc

df = pd.json_normalize(data)
for col in df.columns:
    df[col] = df[col].astype(str)

h5File = "all_indexes.h5"
df.to_hdf(h5File, "/data/d1")

os.system("rm -rf TENDL-2019")
os.system("rm -rf ENDFB-8.0-NNDC")
