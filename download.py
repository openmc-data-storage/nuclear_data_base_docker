
import openmc_data_downloader as odd


odd.download_cross_section_data(
    libraries='TENDL-2019',
    elements='all',
    destination='TENDL-2019'
)

odd.download_cross_section_data(
    libraries='ENDFB-8.0-NNDC',
    elements='all',
    destination='ENDFB-8.0-NNDC',
)
