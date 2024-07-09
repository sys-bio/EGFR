
import matplotlib.pyplot as plt
import tellurium as te


r = te.loada('EGFR_new.ant')

fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 12))


dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
dose_ras = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
times = [240]


egfr = [1.14, 0.01, 2.91, 3.22, 10.41, 19.8, 25.91, 24.81, 33.14]
garem = [0.26, 0.61, 0.78, 0.93, 1.37, 2.0, 1.73, 1.76, 1.81]
gab = [0.0, 0.11, 0.09, 1.09, 2.4, 3.3, 3.23, 2.78, 2.96]
shc = [0.0, 0.13, 0.63, 1.12, 2.83, 5.63, 6.0, 5.51, 5.76]
shp = [0.0, 0.0, 0.0, 2.13, 4.53, 5.70, 4.86, 3.44, 3.93]
sos = [0.01, 0.02, 0.05, 0.12, 0.36, 0.47, 0.5, 0.37, 0.5]
rsk = [0.22, 0.76, 0.82, 7.01, 20.89, 21.66, 22.41, 20.23, 30.00]
# ras = [1.43, 5.38, 13.43, 22.8, 27.78, 28.0, 30.43, 33.65]
ras = [2.02, 4.91, 10.08, 13.9, 17.58, 18.67, 19.50, 19.17, 19.6]

fit_egfr = []
fit_garem = []
fit_gab = []
fit_shc = []
fit_shp = []
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
                                               'pSHC1tot', 'pShp2tot', 'aRas'])
    fit_egfr.append(sim['pEGFRtot'][2400])
    fit_garem.append(sim['pGAREMtot'][2400])
    fit_gab.append(sim['pGAB1tot'][2400])
    fit_shc.append(sim['pSHC1tot'][2400])
    fit_shp.append(sim['pShp2tot'][2400])

for i in range(len(dose_ras)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 720, 7201, selections=['time', 'pEGFRtot', 'pGAREMtot', 'pGAB1tot',
                                               'pSHC1tot', 'pShp2tot', 'aRas'])
    fit_ras.append(sim['aRas'][2400])

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
ax[1, 1].scatter(dose, shp, label='data')
ax[1, 1].scatter(dose, fit_shp, label='fit')
ax[1, 1].title.set_text('Shp')

ax[1, 2].set_xscale('log')
ax[1, 2].scatter(dose_ras, ras, label='data')
ax[1, 2].scatter(dose_ras, fit_ras, label='fit')
ax[1, 2].title.set_text('Ras')

ax[0, 0].legend()
ax[0, 1].legend()
ax[0, 2].legend()
ax[1, 0].legend()
ax[1, 1].legend()
ax[1, 2].legend()

plt.show()
