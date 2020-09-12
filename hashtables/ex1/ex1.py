
def get_indices_of_item_weights(weights, length, limit):
    
    ## loop over wieghts and place in a dictionary
    
    ## index each weight (enumerate)
    
    ## run over which pair of weights equals limit
    
    d = {}

    for index, weight in enumerate(weights): ##make hash table of values in array 
        d[weight] = index

    for i, weight in enumerate(weights): ## loop through array
        if (limit-weight) in d: ## if limit - weight = 0 and is in weights return indexes
            return [d[limit-weight], i]
    return None ## if not found return none



