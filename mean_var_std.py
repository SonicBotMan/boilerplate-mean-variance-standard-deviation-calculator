import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape(3, 3)
    result = {}
    for fn, name in [(np.mean, 'mean'), (np.var, 'variance'), (np.std, 'standard deviation'),
                     (np.max, 'max'), (np.min, 'min'), (np.sum, 'sum')]:
        result[name] = [fn(arr, axis=0).tolist(), fn(arr, axis=1).tolist(), fn(arr).item()]
    return result
