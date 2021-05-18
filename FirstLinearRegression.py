#Simple linear regression
#y = mx + b
#Slope formula:[Sigma((x-x(mean))*(y-y(mean)))/Sigma((x-x(mean)**2)]
#Intercept formula:[(0-(slope*x(mean)))+y_mean]
y_array = ["2","4","5"]
x_array = ["1","2.5","3"]
y2 = []
x2 = []
Exy = 0
y_mean2= 0
x_mean2= 0
x3 = 0
slope2 = 0
intercept2 = 0

def y_mean():
    global y_mean2
    y_mean2 = 0
    for x in range(0, len(y_array)):
        y_mean2 += float(y_array[x])
    y_mean2 = y_mean2/len(y_array)
    return y_mean2

def x_mean():
    global x_mean2
    x_mean2 = 0
    for x in range(0, len(x_array)):
        x_mean2 += float(x_array[x])
    x_mean2 = x_mean2/len(x_array)
    return x_mean2

def slope():
    global y
    global x
    global Exy
    global x3
    global slope2

    for x in range(0, len(y_array)):
        y2.append(float(y_array[x])-y_mean())

    for i in range(0, len(x_array)):
        x2.append(float(x_array[i])-x_mean())
    #Numerator
    if len(y2) == len(x2):
        for x in range(0, len(x2)):
            Exy += y2[x]*x2[x]  
    else:
        print("[LENGTH OF THE X AND Y VARIABLES ARE NOT EQUAL]")        
    #Denominator
    for x in range(0, len(x2)):
        x3 += int(x2[x]**2)

    #Slope
    slope2 = Exy/x3
    return slope2

def intercept():
    #Intercept
    global intercept2
    slope2 = slope()
    intercept2 = 0-(slope2*x_mean())+y_mean()
    return intercept2

def predict(x):
    y_predicted = slope()*x+intercept()
    print(y_predicted)

predict(10)
