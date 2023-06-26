import openmc
import openmc_data_downloader as odd


mat = openmc.Material()
for isotope in odd.ALL_ISOTOPE_OPTIONS:
    mat.add_nuclide(isotope, 1)
mats = openmc.Materials([mat])

mats.download_cross_section_data(
    libraries=["ENDFB-8.0-NNDC"],
    destination="ENDFB-8.0-NNDC",
)

mats.download_cross_section_data(
    libraries=["TENDL-2019"],
    destination="TENDL-2019"
)

