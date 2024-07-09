
import tellurium as te

module_list = ['EGFR_new.ant', 'EGFR_new_no_Shp.ant']

for module in module_list:
    r = te.loada(module)
    r.exportToSBML(module[:-4] + '.xml')
