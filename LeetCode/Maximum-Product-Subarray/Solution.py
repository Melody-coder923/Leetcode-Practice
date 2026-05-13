for i in [0...nums-1]: 
    for j in [i..nums-1]: 
        accumulator = 1
        for k in [i..j]:
            accumulator = accumulator * nums[k]
        result = max(result, accumulator)