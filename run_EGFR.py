
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math

# egfr_datafile = 'egfr.txt'
# 
# egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
# egfr_time = np.array(egfr_df['Time'])
# egfr = np.array(egfr_df['aRtot'])

# l2_datafile = 'level2_.txt'
#
# l2_df = pd.read_csv(l2_datafile, delimiter=r"\s+")
# l2_time = np.array(l2_df['Time'])
# # garem_fit = np.array(l2_df['aR_Grb2_ppGarem'])
# garem_out = np.array(l2_df['aR_Grb2_ppGarem_pShp2'])
# # gab_fit = np.array(l2_df['aR_Grb2_ppGab1'])
# gab_out = np.array(l2_df['aR_Grb2_ppGab1_pShp2'])
# shc = np.array(l2_df['aR_pShc1'])

# r = te.loada('EGFR_module2.ant')
# r = te.loada('EGFR_module.ant')
# r = te.loada('EGFR_module_hsw_simplex.ant')
# r = te.loada('EGFR_module_hsw.ant')
# r = te.loada('EGFR_module_hsw_0.ant')
# r = te.loada('EGFR_module_hsw_1.ant')
# r = te.loada('EGFR_module_hsw_2.ant')
# r = te.loada('EGFR_module_hsw_3.ant')
# r = te.loada('EGFR_module_hsw_4.ant')
# r = te.loada('EGFR_module_hsw_5.ant')
# r = te.loada('EGFR_module_hsw_6.ant')
# r = te.loada('EGFR_module_hsw_best.ant')
# r = te.loada('EGFR_module_hsw_simplex_oiv_kin_dose.ant')
# r = te.loada('EGFR_module_hsw_simplex_niv_kin_dose.ant')
# r = te.loada('EGFR_module_hsw_de_2fold_oiv_kin_dose.ant')
# r = te.loada('EGFR_module_hsw_nocomp.ant')
# r = te.loada('EGFR_sequential_fit_egfr.ant')
# r = te.loada('EGFR_4_HSW.ant')
# r = te.loada('EGFR_5_HSW_MK_rev.ant')
# r = te.loada('EGFR_5_HSW_MK_rev_2.ant')
# r = te.loada('EGFR_5_HSW_MK_rev_3.ant')
r = te.loada('EGFR_8b.ant')
# r = te.loada('EGFR_8b_1.ant')

# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
# sim = r.simulate(0, 12, 1201, selections=['time', 'Lig', 'aRtot'])
# sim = r.simulate(0, 720, 7201, selections=['time', 'aR_Grb2_ppGarem', 'aR_Grb2_ppGarem_pShp2', 'aR_Grb2_ppGab1',
#                                            'aR_Grb2_ppGab1_pShp2', 'aR_pShc1'])
# print(sim)
# t = np.linspace(0, 720, 7201)

# print(r.steadyState())
# print(sim)
# quit()
# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')

# fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(16, 12))
#
# ax[0, 0].plot(t, sim['aR_Grb2_ppGarem'], label='Garem fit')
# ax[0, 0].scatter(l2_time, garem_fit, label='Garem fit data')
#
# ax[0, 1].plot(t, sim['aR_Grb2_ppGarem_pShp2'], label='Garem out')
# ax[0, 1].scatter(l2_time, garem_out, label='Garem out data')
#
# ax[1, 0].plot(t, sim['aR_Grb2_ppGab1'], label='Gab fit')
# ax[1, 0].scatter(l2_time, gab_fit, label='Gab fit data')
#
# ax[1, 1].plot(t, sim['aR_Grb2_ppGab1_pShp2'], label='Gab out')
# ax[1, 1].scatter(l2_time, gab_out, label='Gab out data')
#
# ax[2, 0].plot(t, sim['aR_pShc1'], label='Shc')
# ax[2, 0].scatter(l2_time, shc, label='Shc data data')
#
# # ax[0, 0].title.set_text('time series')
# ax[0, 0].legend()
# ax[1, 0].legend()
# ax[0, 1].legend()
# ax[1, 1].legend()
# ax[2, 0].legend()

# plt.plot(t, sim['aR_Grb2_ppGarem'], label='Garem fit')
# plt.scatter(l2_time, garem_fit, label='Garem fit data')
#
# plt.plot(t, sim['aR_Grb2_ppGarem_pShp2'], label='Garem out')
# plt.scatter(l2_time, garem_out, label='Garem out data')
#
# plt.plot(t, sim['aR_Grb2_ppGab1'], label='Gab fit')
# plt.scatter(l2_time, gab_fit, label='Gab fit data')
#
# plt.plot(t, sim['aR_Grb2_ppGab1_pShp2'], label='Gab out')
# plt.scatter(l2_time, gab_out, label='Gab out data')
#
# plt.plot(t, sim['aR_pShc1'], label='Shc')
# plt.scatter(l2_time, shc, label='Shc data data')
#
# plt.title('time series')
# plt.legend()

fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 12))


dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
dose_ras = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95]
times = [240]
# response1 = [[0.22], [0.28], [0.31], [0.33], [0.41], [0.52], [0.47], [0.47], [0.48]]
# response2 = [[0.51], [0.65], [0.72], [0.78], [0.95], [1.2], [1.1], [1.11], [1.13]]
# response3 = [[0.18], [0.19], [0.19], [0.29], [0.42], [0.51], [0.5], [0.46], [0.48]]
# response4 = [[0.41], [0.45], [0.45], [0.68], [0.98], [1.19], [1.17], [1.07], [1.11]]
# response5 = [[1.69], [1.76], [2.15], [2.53], [3.85], [6.01], [6.3], [5.92], [6.11]]

# # response1 = [0.22, 0.28, 0.31, 0.33, 0.41, 0.52, 0.47, 0.47, 0.48]
# response2 = [0.51, 0.65, 0.72, 0.78, 0.95, 1.2, 1.1, 1.11, 1.13]
# # response3 = [0.18, 0.19, 0.19, 0.29, 0.42, 0.51, 0.50, 0.46, 0.48]
# response4 = [0.41, 0.45, 0.45, 0.68, 0.98, 1.19, 1.17, 1.07, 1.11]
# response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]

# response2 = [0.726, 0.925, 1.027, 1.11, 1.361, 1.72, 1.567, 1.581, 1.612]
# response4 = [0.59, 0.65, 0.64, 0.97, 1.4, 1.7, 1.68, 1.53, 1.59]
# response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]

egfr = [1.14, 0.01, 2.91, 3.22, 10.41, 19.8, 25.91, 24.81, 33.14]
garem = [0.22, 0.52, 0.67, 0.8, 1.18, 1.72, 1.49, 1.51, 1.56]
gab = [0.0, 0.06, 0.05, 0.56, 1.23, 1.7, 1.66, 1.43, 1.53]
shc = [0.0, 0.13, 0.66, 1.18, 2.97, 5.91, 6.3, 5.78, 6.05]
shp = [2.41, 2.74, 3.25, 3.78, 5.32, 8.02, 9.1, 8.04, 6.84]
sos = [0.01, 0.02, 0.05, 0.12, 0.36, 0.47, 0.5, 0.37, 0.5]
rsk = [0.22, 0.76, 0.82, 7.01, 20.89, 21.66, 22.41, 20.23, 30.00]
ras = [1.43, 5.38, 13.43, 22.8, 27.78, 28.0, 30.43, 33.65]
# ras = [0.67, 0.95, 3.17, 5.76, 10.61, 16.05, 19.87, 19.18]

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
                                               'pSHC1tot', 'pShp2tot', 'aRAStot'])
#     fit240.append(sim[2400][1])
    print(sim['time'][2400])
    fit_egfr.append(sim['pEGFRtot'][2400])
    fit_garem.append(sim['pGAREMtot'][2400])
    fit_gab.append(sim['pGAB1tot'][2400])
    fit_shc.append(sim['pSHC1tot'][2400])
    fit_shp.append(sim['pShp2tot'][2400])
    # fit_sos.append(sim['pSOS1'][2400])
    # fit_rsk.append(sim['aRSK'][2400])
    # fit_gs.append(sim['Grb2_SOS1'][2400])
    # fit_ras.append(sim['aRAStot'][2400])

for i in range(len(dose_ras)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 720, 7201, selections=['time', 'pEGFRtot', 'pGAREMtot', 'pGAB1tot',
                                               'pSHC1tot', 'pShp2tot', 'aRAStot'])
#     fit240.append(sim[2400][1])
    print(sim['time'][2400])
    # fit_egfr.append(sim['pEGFRtot'][2400])
    # fit_garem.append(sim['pGAREMtot'][2400])
    # fit_gab.append(sim['pGAB1tot'][2400])
    # fit_shc.append(sim['pSHC1tot'][2400])
    # fit_sos.append(sim['pSOS1'][2400])
    fit_ras.append(sim['aRAStot'][2400])

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
ax[1, 1].scatter(dose, shp, label='data')
ax[1, 1].scatter(dose, fit_shp, label='fit')
ax[1, 1].title.set_text('Shp')

# ax[1, 1].set_xscale('log')
# ax[1, 1].scatter(dose, sos, label='data')
# ax[1, 1].scatter(dose, fit_sos, label='fit')
# ax[1, 1].title.set_text('Sos')

# ax[1, 2].set_xscale('log')
# ax[1, 2].scatter(dose, rsk, label='data')
# ax[1, 2].scatter(dose, fit_rsk, label='fit')
# ax[1, 2].title.set_text('Rsk')

ax[1, 2].set_xscale('log')
ax[1, 2].scatter(dose_ras, ras, label='data')
ax[1, 2].scatter(dose_ras, fit_ras, label='fit')
ax[1, 2].title.set_text('Ras')

# ax[2, 1].set_xscale('log')
# ax[2, 1].scatter(dose, fit_gs, label='fit')
# ax[2, 1].title.set_text('Grb2_SOS1')
#
#     ax[1, 0].plot(sim_times, fit_response2, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response2[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response3, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response3[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response4, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response4[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response5, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response5[i], color=color)
#
#     ax[1, 0].title.set_text('dose response (time series)')

ax[0, 0].legend()
ax[0, 1].legend()
ax[0, 2].legend()
ax[1, 0].legend()
ax[1, 1].legend()
ax[1, 2].legend()

plt.show()
quit()

# dose1 = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
# response1 = [0.22, 0.28, 0.31, 0.33, 0.41, 0.52, 0.47, 0.47, 0.48]
# response2 = [0.51, 0.65, 0.72, 0.78, 0.95, 1.2, 1.1, 1.11, 1.13]
# response3 = [0.18, 0.19, 0.19, 0.29, 0.42, 0.51, 0.50, 0.46, 0.48]
# response4 = [0.41, 0.45, 0.45, 0.68, 0.98, 1.19, 1.17, 1.07, 1.11]
# response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]
#
# fit1 = []
# fit2 = []
# fit3 = []
# fit4 = []
# fit5 = []

# print(fit240)
# ax[0, 1].set_xscale('log')
# ax[0, 1].scatter(dose1, response1)
# ax[0, 1].scatter(dose1, fit240)
# t1 = np.linspace(0, 240, 2501)
# for i in range(len(dose)):
#     r.reset()
#     r.Lig = dose[i]
#     sim = r.simulate(0, 240, 2501, selections=['time', 'aRtot', 'Egfr', 'iEgfr'])
#     ax[1][0].plot(t1, sim['aRtot'], label=str(dose[i]))
#     ax[1][0].scatter(240, response[i])
#
# ax[1][0].title.set_text('dose response (time curves)')
# ax[1][0].legend(loc='upper center')
ax[0, 1].title.set_text('dose response')

plt.show()
