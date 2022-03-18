from sklearn.metrics import det_curve
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
The function ssklearn.metrics.det_curve(y_true, y_score, pos_label=None, sample_weight=None)
returns fpr, fnr, thresholds

"""
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, fnr, thresholds = det_curve(y_true, y_scores)
print(fpr)
def compute_FPR_FNR():
    pass