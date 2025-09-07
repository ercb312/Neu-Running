import numpy as np

def compute_rmssd(rr_intervals):
    """HRV 지표 RMSSD 계산"""
    rr_diff = np.diff(rr_intervals)
    return np.sqrt(np.mean(rr_diff**2))
