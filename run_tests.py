import numpy as np
from hydromodels import hydromodels

gr4j = hydromodels.GR4J({'X1': 10, 'X2': 4, 'X3': 3, 'X4': 2})
print(gr4j)
print(gr4j.run(np.array([10,20,30,40.]), np.array([1,2,3,4.])))
