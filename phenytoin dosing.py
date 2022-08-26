import numpy as np

#solve non-linear kinetic problem using system of equation
S = float(input('input the salt factor: '))
w = float(input('input patient weight (kg): '))
D1 = float(input('input the 1st dose (mg/d): '))
Css1 = float(input('input the 1st steady state concentration (mg/L): '))
D2 = float(input('input the 2nd dose (mg/d): '))
Css2 = float(input('input the 2nd steady state concentration (mg/L): '))
Vd = 0.7*w
A = np.array([[Css1,-S*D1],[Css2,-S*D2]])
B = np.array([S*D1*Css1,S*D2*Css2])

X = np.linalg.solve(A,B)
Vmax = round(X[0])
Km = round(X[1])
print('Vmax : ' + str(Vmax))
print('Km: '+ str(Km))

#calculate new dose for phenytoin sodium
desiredC= float(input('input the new desired steady state concentration (mg/L): '))
newD = (Vmax*desiredC)/(S*(Km + desiredC))
D = round(newD)
print('the calculated dose is: '+ str(D))
recommendedD = input('input the recommended dose based on the calculated dose: ')

#calculate the amount of time need to achieve 90% of steady state concentration
t90 = round((Km*Vd*(2.3*Vmax-0.9*float(recommendedD)*S))/((Vmax-newD*S)**2))
print('t90% is: ' +str(t90)+' day')

