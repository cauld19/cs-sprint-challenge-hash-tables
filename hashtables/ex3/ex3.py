def intersection(arrays):
    arr = []
    cache = {}
    
    
    for index, value in enumerate(arrays): ##make hash table of values in array 
        for j, number in enumerate(value):
            # print(arrays[index])
            # print(value[j])

            if value[j] not in cache:
                cache[value[j]] = 0
            else:
                cache[value[j]] += 1

    for key, value in cache.items():
        if value > 0:
            arr.append(key)        
                 
    return arr


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 15)) + [1, 2, 3])
    arrays.append(list(range(20, 25)) + [1, 2, 3])
    arrays.append(list(range(30, 35)) + [1, 2, 3])

    print(intersection(arrays))
