# Python code for generating the panel subplots I mentioned, based on template lg results (attached):
from scipy.stats import pearsonr
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#matplotlib.use("Agg")


SMALL_SIZE = 14
MEDIUM_SIZE = 16
MEDIUM_LARGE_SIZE = 18
BIG_SIZE = 20
JUMBO_SIZE = 22

# Number of predicted atom-based cases from each theory
# plt.subplot(1,2,1)
xlg_empirical = np.append(
    float(271)/(271+63), float(323)/(323+11)*np.ones(8))*100
uid = (np.asarray([6, 7, 8, 6, 8, 7, 6, 8, 5])/float(9))*100
rig = (np.asarray([3, 8, 9, 9, 9, 9, 9, 9, 8])/float(9))*100
inds = [11, 21, 31, 41, 51, 61, 71, 81, 91]
plt.plot(inds, xlg_empirical, 'x-')
plt.plot(inds, uid, 'o:')
plt.plot(inds, rig, 's--')
plt.legend(['Cross-language empirical', 'UID prediction',
            'RIG prediction'], fontsize=MEDIUM_LARGE_SIZE)
plt.xlabel('Numerical range', fontsize=BIG_SIZE + 2)
plt.ylabel('Base-atom case ({0})'.format("%"), fontsize=BIG_SIZE + 2)
plt.xticks(fontsize=MEDIUM_LARGE_SIZE)
plt.yticks(fontsize=MEDIUM_LARGE_SIZE)

[corr_uid, pval_uid] = scipy.stats.pearsonr(xlg_empirical, uid)
[corr_rig, pval_rig] = scipy.stats.pearsonr(xlg_empirical, rig)
plt.tight_layout()

print('corr(empirical,UID) = ', str(corr_uid), ' p-value = ', str(pval_uid))
print('corr(empirical,RIG) = ', str(corr_rig), ' p-value = ', str(pval_rig))
plt.savefig("middle-panel_1.png")
plt.savefig("middle-panel_1.eps")

# % of cases that base-atom information profile is elbowing below (as opposed to over) UID straightline
# plt.subplot(1,2,2)
"""inds = [11, 21, 31, 41, 51, 61, 71, 81, 91]
rig1 = (np.asarray([3, 9, 9, 8, 9, 9, 9, 9, 8])/float(9))*100
plt.bar(inds, rig1, width=5, color='black')
plt.xlabel('Numerical range', fontsize=BIG_SIZE + 2)
plt.ylabel('RIG-conforming case ({0})'.format("%"), fontsize=BIG_SIZE + 2)
plt.xticks(fontsize=MEDIUM_LARGE_SIZE)
plt.yticks(fontsize=MEDIUM_LARGE_SIZE)
plt.tight_layout()

plt.savefig("middle-panel_2.png")
plt.savefig("middle-panel_2.eps")"""

# Statistics:
# corr(empirical,UID) =  0.775  p-value <  0.02
# corr(empirical,RIG) =  0.904  p-value <  0.001
