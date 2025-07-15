def log(msg):
    print(f"[LOG] {msg}")

def normalize_array(arr):
    min_val = arr.min()
    max_val = arr.max()
    norm = (arr - min_val) / (max_val - min_val)
    return norm, min_val, max_val