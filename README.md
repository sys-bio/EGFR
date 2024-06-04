
### INSTALLATION

if you use conda
https://docs.anaconda.com/free/anaconda/install/index.html

`conda create -n egfr python==3.10.12`

`conda activate egfr`

You only need to pip install the pybionetfit package for fitting

pybionetfit requires Python<=3.5

`pip install pybnf`

Install tellurium for analysis

`pip install tellurium`

### RUN PYBIONETFIT
make sure you cd into the correct directory

`pybnf -c EGFR_pybionetfit.conf`

### INSERT PARAMETERS

`python insert_x_params.py <x = EGFR, EGFR_no_Shp>`

### PLOT RESULTS

`python run_EGFR_x.py <x = EGFR, EGFR_no_Shp>`
