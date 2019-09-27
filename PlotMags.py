#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

def runRANSAC(df, maglimit, iterations):
    X = []
    y = []
    Gx = []
    Gy = []

    for i in range(len(df.index)):
        if df.loc[i,'GMAG'] > 0 and df.loc[i,'GMAG'] < maglimit:
            #print df.loc[i,'GMAG']
            X.append(df.loc[i,'GMAG'])
            y.append(df.loc[i,'MAG'])
            Gx.append(df.loc[i,'RA'])
            Gy.append(df.loc[i,'DEC'])

    X = np.reshape(X,(-1,1))
    y = np.reshape(y,(-1,1))

    line_y_ransac_tmp = []
    line_X = np.arange(X.min(), X.max())[:, np.newaxis]

    for i in range(iterations):
        # Robustly fit linear model with RANSAC algorithm
        ransac = linear_model.RANSACRegressor(residual_threshold=0.5, stop_probability=0.9999)
        ransac.fit(X, y)
        inlier_mask = ransac.inlier_mask_
        outlier_mask = np.logical_not(inlier_mask)
        line_y_ransac = ransac.predict(line_X)
        line_y_ransac_tmp.append(line_y_ransac)

    line_y_ransac = np.mean(line_y_ransac_tmp,axis=0)

    return X, y, line_y_ransac, line_X, inlier_mask, outlier_mask
    # Predict data of estimated models

pklfile = sys.argv[1]

df = pd.read_pickle(pklfile)
df = df[(df.MAG < 0) & (df.GMAG < 15)]
df = df.reset_index(drop=True)

#for i in range(len(df.index)):
#    print(df.loc[i,'FLUX'], df.loc[i,'MAG'], df.loc[i,'GMAG'])

X, y, line_y_ransac, line_X, inlier_mask, outlier_mask = runRANSAC(df, 9, 100)
X15, y15, line_y_ransac15, line_X15, inlier_mask15, outlier_mask15 = runRANSAC(df, 15, 100)


mR = (line_y_ransac[len(line_y_ransac)-1]-line_y_ransac[0]) / (line_X[len(line_X)-1]-line_X[0])
bR = line_y_ransac[0]-mR*line_X[0]
print(mR, bR)

b = y-X
print(np.mean(b))

#plt.scatter(Gx, Gy, color='r', alpha=0.3)

plt.figure(figsize=(14,10))

# plt.scatter(df['GMAG'],df['MAG'], marker='o', color='black')

plt.scatter(df.GMAG, df.MAG)
plt.scatter(X[outlier_mask], y[outlier_mask], color='gold', marker='o', edgecolors='black', label='Outliers')
plt.scatter(X[inlier_mask], y[inlier_mask], color='yellowgreen', marker='o', edgecolors='black', label='Inliers')
plt.plot(line_X, line_y_ransac, color='cornflowerblue', linewidth=2, label='y={0:0.2f}'.format(mR[0]) + '*' + r'M$_\mathrm{G}$' + ' + {0:0.2f}'.format(bR[0]) + ' (RANSAC)')
plt.xlim(4,15)
plt.ylim(-16,-4)
# plt.ylim(0,0.00000000001)
# plt.title('Instrumental Magnitude vs GAIA DR2 G Magnitude')
plt.xlabel('GAIA G-band Magnitude', size=15)
plt.ylabel('Instrumental Magnitude', size=15)
plt.legend()

plt.tight_layout()
plt.savefig('IMag-vs-GMag-EMCCD.png', dpi=300)

plt.show()


# In[ ]:





# In[ ]:




