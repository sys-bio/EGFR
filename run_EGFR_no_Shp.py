
import matplotlib.pyplot as plt
import tellurium as te


r = te.loada('EGFR_no_Shp.ant')

fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 12))

dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
dose_ras = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95]
times = [240]

egfr = [1.14, 0.01, 2.91, 3.22, 10.41, 19.8, 25.91, 24.81, 33.14]
garem = [0.22, 0.52, 0.67, 0.8, 1.18, 1.72, 1.49, 1.51, 1.56]
gab = [0.0, 0.06, 0.05, 0.56, 1.23, 1.7, 1.66, 1.43, 1.53]
shc = [0.0, 0.13, 0.66, 1.18, 2.97, 5.91, 6.3, 5.78, 6.05]
sos = [0.01, 0.02, 0.05, 0.12, 0.36, 0.47, 0.5, 0.37, 0.5]
rsk = [0.22, 0.76, 0.82, 7.01, 20.89, 21.66, 22.41, 20.23, 30.00]
ras = [0.67, 0.95, 3.17, 5.76, 10.61, 16.05, 19.87, 19.18]

fit_egfr = []
fit_garem = []
fit_gab = []
fit_shc = []
fit_sos = []
fit_rsk = []
fit_ras = []
fit_gs = []

fit_response = []
fit240 = []
for i in range(len(dose)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 720, 7201, selections=['time', 'pEGFRtot', 'pGAREMtot', 'pGAB1tot',
                                               'pSHC1tot', 'aRas3'])
    fit_egfr.append(sim['pEGFRtot'][2400])
    fit_garem.append(sim['pGAREMtot'][2400])
    fit_gab.append(sim['pGAB1tot'][2400])
    fit_shc.append(sim['pSHC1tot'][2400])

for i in range(len(dose_ras)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 720, 7201, selections=['time', 'pEGFRtot', 'pGAREMtot', 'pGAB1tot',
                                               'pSHC1tot', 'aRas3'])
    fit_ras.append(sim['aRas3'][2400])

# color = next(ax[1, 0]._get_lines.prop_cycler)['color']

ax[0, 0].set_xscale('log')
ax[0, 0].scatter(dose, egfr, label='data')
ax[0, 0].scatter(dose, fit_egfr, label='fit')
ax[0, 0].title.set_text('Egfr')

ax[0, 1].set_xscale('log')
ax[0, 1].scatter(dose, garem, label='data')
ax[0, 1].scatter(dose, fit_garem, label='fit')
ax[0, 1].title.set_text('Garem')

ax[0, 2].set_xscale('log')
ax[0, 2].scatter(dose, gab, label='data')
ax[0, 2].scatter(dose, fit_gab, label='fit')
ax[0, 2].title.set_text('Gab')

ax[1, 0].set_xscale('log')
ax[1, 0].scatter(dose, shc, label='data')
ax[1, 0].scatter(dose, fit_shc, label='fit')
ax[1, 0].title.set_text('Shc')

ax[1, 1].set_xscale('log')
ax[1, 1].scatter(dose_ras, ras, label='data')
ax[1, 1].scatter(dose_ras, fit_ras, label='fit')
ax[1, 1].title.set_text('Ras')

ax[0, 0].legend()
ax[0, 1].legend()
ax[0, 2].legend()
ax[1, 0].legend()
ax[1, 1].legend()

plt.show()
