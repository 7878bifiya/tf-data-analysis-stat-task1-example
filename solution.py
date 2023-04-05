import pandas as pd
import numpy as np
from scipy import stats
from scipy.optimize import minimize_scalar

chat_id = 541133397 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mean = np.mean(checks)
    ratio = mean / 371
    omega_squared = np.log(1 + (np.std(checks)/mean)**2)
    a = ratio * np.exp(omega_squared/2)
    return a
