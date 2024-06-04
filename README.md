
### INSTALLATION

if you use conda
https://docs.anaconda.com/free/anaconda/install/index.html

`conda create -n egfr python==3.10.12`

`conda activate egfr`

You only need to pip install the pybionetfit package
pybionetfit requires Python<=3.5

`pip install pybnf`

### ENVIRONMENT

packages in environment at /home/michael/anaconda3/envs/egfr:

| Name | Version |
- _libgcc_mutex             0.1
- _openmp_mutex             5.1
- bcrypt                    4.1.3
- bzip2                     1.0.8
- ca-certificates           2024.3.11
- cffi                      1.16.0
- click                     8.1.7
- cloudpickle               3.0.0
- cryptography              42.0.7
- dask                      2022.12.1
- distributed               2022.12.1
- fsspec                    2024.3.1
- jinja2                    3.1.4
- ld_impl_linux-64          2.38
- libffi                    3.4.4
- libgcc-ng                 11.2.0
- libgomp                   11.2.0
- libroadrunner             2.7.0
- libstdcxx-ng              11.2.0
- libuuid                   1.41.5
- locket                    1.0.0
- markupsafe                2.1.5
- msgpack                   0.6.2
- ncurses                   6.4
- nose                      1.3.7
- numpy                     1.26.4
- openssl                   3.0.13
- packaging                 24.0
- paramiko                  3.4.0
- partd                     1.4.2
- pip                       24.0
- psutil                    5.9.8
- pybnf                     1.2.2
- pycparser                 2.22
- pynacl                    1.5.0
- pyparsing                 3.1.2
- python                    3.10.12
- pyyaml                    6.0.1
- readline                  8.2
- scipy                     1.13.0
- setuptools                69.5.1
- sortedcontainers          2.4.0
- sqlite                    3.45.3
- tblib                     3.0.0
- tk                        8.6.14 
- toolz                     0.12.1
- tornado                   6.4
- tzdata                    2024a
- urllib3                   2.2.1
- wheel                     0.43.0
- xz                        5.4.6
- zict                      3.0.0
- zlib                      1.2.13

### RUN PYBIONETFIT
make sure you cd into the correct directory

`pybnf -c EGFR_x_de.conf> x = EGFR, EGFR_no_Shp`

### INSERT PARAMETERS

`python insert_x_params.py> x = EGFR, EGFR_no_Shp`

### PLOT RESULTS

`python run_EGFR_x.py> x = EGFR, EGFR_no_Shp`
