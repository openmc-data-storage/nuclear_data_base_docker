
A Dockerfile for containing nuclear data:
- The nuclear data has been split up into seperate files
- There is one file for every reaction in each isotope
- There are also index files that identify all the reaction files available

build with:

```bash
docker build -t nuclear_data_base_docker .
```

The Docker image generated is used as a base image for [xsplot.com](https://github.com/openmc-data-storage/xsplot.com)
