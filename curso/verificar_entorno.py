
import sys
import numpy as np
import pandas as pd
import scipy
import sklearn
import matplotlib

print('Python', sys.version.split()[0])
for modulo in (np, pd, scipy, sklearn, matplotlib):
    print(modulo.__name__, modulo.__version__)