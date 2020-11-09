def dotproduct(V1,V2):
    sum = 0
    for i in range(len(V1)):
        sum += V1[i]*V2[i]
    return(sum)

def length(V):
    sum = 0
    for i in range(len(V)):
        sum += V[i]**2
    return(sum**0.5)

def sim(V1,V2):
    return(dotproduct(V1,V2)/(length(V1)*length(V2)))
