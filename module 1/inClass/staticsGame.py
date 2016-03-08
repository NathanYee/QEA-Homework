location = [-8,-4,-3,2,5,8]
mass = [4,10,10,4,7,8]

def centerOM(x,y):
    numerator = range(len(x))
    for i in range(len(location)):
        numerator[i]=x[i]+y[i]
    return sum(numerator)/sum(y)

print centerOM(location,mass)
