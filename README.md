
A Dockerfile for containing separate JSON files for each individual reactions for a range of libraries

build with:


```bash
docker build -t nuclear_data_base_docker .
```

The Docker image generated is used as a base image for [xsplot.com](https://github.com/openmc-data-storage/xsplot.com)
