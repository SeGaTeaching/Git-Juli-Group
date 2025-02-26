def minus(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    
    return result