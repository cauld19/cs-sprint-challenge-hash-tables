def has_negatives(a):
    cache = {}
    arr = []
    
    arr_sorted = sorted(a,reverse=True)

    for val in arr_sorted:
        if val > 0:
            cache[val] = 0
        elif val < 0 and abs(val) in cache:
            arr.append(abs(val))


    return arr

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
