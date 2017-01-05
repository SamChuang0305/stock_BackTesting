def policy(Open,high,low,close):
    rate = (close - Open)/Open
    if(rate > 0.007):
        return 1
    elif(rate <(-0.007)):
        return -1
    else :
        return 0