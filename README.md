
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

Name                    Version                   Build  Channel 
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
bcrypt                    4.1.3                    pypi_0    pypi
bzip2                     1.0.8                h5eee18b_6  
ca-certificates           2024.3.11            h06a4308_0  
cffi                      1.16.0                   pypi_0    pypi
click                     8.1.7                    pypi_0    pypi
cloudpickle               3.0.0                    pypi_0    pypi
cryptography              42.0.7                   pypi_0    pypi
dask                      2022.12.1                pypi_0    pypi
distributed               2022.12.1                pypi_0    pypi
fsspec                    2024.3.1                 pypi_0    pypi
jinja2                    3.1.4                    pypi_0    pypi
ld_impl_linux-64          2.38                 h1181459_1  
libffi                    3.4.4                h6a678d5_1  
libgcc-ng                 11.2.0               h1234567_1  
libgomp                   11.2.0               h1234567_1  
libroadrunner             2.7.0                    pypi_0    pypi
libstdcxx-ng              11.2.0               h1234567_1  
libuuid                   1.41.5               h5eee18b_0  
locket                    1.0.0                    pypi_0    pypi
markupsafe                2.1.5                    pypi_0    pypi
msgpack                   0.6.2                    pypi_0    pypi
ncurses                   6.4                  h6a678d5_0  
nose                      1.3.7                    pypi_0    pypi
numpy                     1.26.4                   pypi_0    pypi
openssl                   3.0.13               h7f8727e_1  
packaging                 24.0                     pypi_0    pypi
paramiko                  3.4.0                    pypi_0    pypi
partd                     1.4.2                    pypi_0    pypi
pip                       24.0            py310h06a4308_0  
psutil                    5.9.8                    pypi_0    pypi
pybnf                     1.2.2                    pypi_0    pypi
pycparser                 2.22                     pypi_0    pypi
pynacl                    1.5.0                    pypi_0    pypi
pyparsing                 3.1.2                    pypi_0    pypi
python                    3.10.12              h955ad1f_0  
pyyaml                    6.0.1                    pypi_0    pypi
readline                  8.2                  h5eee18b_0  
scipy                     1.13.0                   pypi_0    pypi
setuptools                69.5.1          py310h06a4308_0  
sortedcontainers          2.4.0                    pypi_0    pypi
sqlite                    3.45.3               h5eee18b_0  
tblib                     3.0.0                    pypi_0    pypi
tk                        8.6.14               h39e8969_0  
toolz                     0.12.1                   pypi_0    pypi
tornado                   6.4                      pypi_0    pypi
tzdata                    2024a                h04d1e81_0  
urllib3                   2.2.1                    pypi_0    pypi
wheel                     0.43.0          py310h06a4308_0  
xz                        5.4.6                h5eee18b_1  
zict                      3.0.0                    pypi_0    pypi
zlib                      1.2.13               h5eee18b_1

### RUN PYBIONETFIT
make sure you cd into the correct directory
`pybnf -c EGFR_x_de.conf> x = EGFR, EGFR_no_Shp`

### INSERT PARAMETERS

`python insert_x_params.py> x = EGFR, EGFR_no_Shp`

### PLOT RESULTS

`python run_EGFR_x.py> x = EGFR, EGFR_no_Shp`
