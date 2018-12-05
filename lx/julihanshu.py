def myabs(x):
    if not isinstance(x,(int,float)):
        raise chucuole    
    if x>0:
        return x
    else:
        return -x
