
import pandas as pd
import tellurium as te

data = None

with open('Results/sorted_params_final.txt', 'r') as file:
    data = file.read().replace('#', '')

with open('parameters', 'w') as params:
    params.write(data)

params_df = pd.read_csv('parameters', delim_whitespace=True)

names = list(params_df.columns)
best = list(params_df.iloc[0])
names = names[2:]
best = best[2:]

param_dict = dict()
for i, name in enumerate(names):
    param_dict[name] = best[i]

model_name = 'EGFR_new_no_Shp'

new_model = ''
with open(model_name + '.ant', 'r') as model:
    lines = model.readlines()
    for i, line in enumerate(lines):
        line_split = line[:-1].strip().split()
        if line_split and line_split[0] in param_dict:
            line_split[2] = str(param_dict[line_split[0]])
        line = ' '.join(line_split) + '\n'
        new_model += line

with open(model_name + '.ant', 'w') as cur_mod:
    cur_mod.write(new_model)

r = te.loada(model_name + '.ant')
r.exportToSBML(model_name + '.xml')
