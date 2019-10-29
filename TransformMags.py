import numpy as np
import scipy.optimize as optimize

imag = np.array([10.173, 11.649, 11.154, 11.819, 10.779, 11.02, 9.882, 10.161, 12.119, 12.969, 12.559, 12.655])
pmag = np.array([11.721, 13.270, 13.231, 14.281, 13.833, 13.347, 12.362, 12.750, 17.230, 16.730, 14.673, 14.681])
# imag = 10.173
# pmag = 11.721
ci = np.array([0.458, 0.481, 0.804, 1.096, 1.484, 0.932, 1.187, 1.208, 2.394, 1.770, 0.831, 0.748])
# ci = 0.458

def magcalc(params):
    tprime, zprime = params
    cmag = np.add(imag,tprime*ci) + zprime # cmag = calculated mag, ci = colour index
    return cmag

def con(params):
    cmag = magcalc(params)
    residual = np.subtract(pmag,cmag)
    print(np.mean(residual))
    return np.mean(residual)

def res(params, imag, ci, pmag):
    cmag = magcalc(params)
    residual = np.subtract(pmag,cmag) # pmag = photometric mag
    stddev = np.std(residual)
    return stddev

cons = {'type':'eq', 'fun': con}

result = optimize.minimize(res, (1.5,0.8), method='SLSQP', constraints=cons, bounds=((0,2),(0,2)), args=(imag,ci,pmag))

print(result)

newmag = imag + result.x[0]*ci + result.x[1]

print(newmag - pmag)