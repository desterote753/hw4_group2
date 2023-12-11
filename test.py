import functions
import pandas as pd
import seaborn as sns

k = 4
data_path = 'pca.csv'
essential_cols = ['0','1','2']
functions.k_means_standard(k, data_path, essential_cols, nrows=10**4, chunksize=10**3, upper_bound_for_iterations=50 )


