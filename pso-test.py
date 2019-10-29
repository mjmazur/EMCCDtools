import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx

def standev():


def magcalc(params):
    tprime, zprime = params
    cmag = np.add(imag,tprime*ci) + zprime # cmag = calculated mag, ci = colour index
    return cmag

def con():
    return mean(residual)

def res(params, imag, ci, pmag):
    cmag = magcalc(params)
    # tprime, zprime = params
    # cmag = np.add(imag,tprime*ci) + zprime
    residual = np.subtract(pmag,cmag) # pmag = photometric mag
    stddev = np.std(residual)
    return abs(stddev)

imag = np.array([10.173, 11.649, 11.154, 11.819, 10.779, 11.02, 9.882, 10.161])
pmag = np.array([11.721, 13.270, 13.231, 14.281, 13.833, 13.347, 12.362, 12.750])
# imag = 10.173
# pmag = 11.721
ci = np.array([0.458, 0.481, 0.804, 1.096, 1.484, 0.932, 1.187, 1.208])
# ci = 0.458

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
# Call instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
# Perform optimization
best_cost, best_pos = optimizer.optimize(fx.sphere, iters=100)