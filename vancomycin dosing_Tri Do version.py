import numpy as np

# Vancomycin dosing project

#Calculate patient's creatinine clearance

while True:
    def getGender():
        while True:
            print('enter patient\'s sex: ')
            gender = input().lower()
            if gender in ['male','female','m','f']:
                return gender
            else:
                print('enter either \'m\' for male or \'f\' for female')
    gender = getGender()

    def getHeight():
        while True:
            print('enter patient\'s height (inch only): ')
            h = input()
            text = 'abcdefghijklmnopqrstuvwxyz`~:;/\|*$#^&()+=-_'
            if h.lower().startswith(tuple(text)):
                print('enter number (in inch) only')
            else:
                return h
    h = float(getHeight())

    def getWeight():
        while True:
            print('input patient\'s weight (kg only): ')
            w = input()
            text1 = 'abcdefghijklmnopqrstuvwxyz`~:;/\|*$#^&()+=-_'
            if w.lower().startswith(tuple(text1)):
                print('enter number (kg) only')
            else:
                return w
    w = float(getWeight())

    def getAge():
        while True:
            print('enter patient\'s age: ')
            age = input()
            a = list(range(200))
            b = []
            for i in a:
                b.append(str(i))
            if age in b:
                return age
            else:
                print('enter whole number only')
    age = float(getAge())

    def getScr():
        while True:
            print('input patient\'s serum creatinine (mg/dL): ')
            Scr = input()
            text2 = 'abcdefghijklmnopqrstuvwxyz`~:;/\|*$#^&()+=-_'
            if Scr.lower().startswith(tuple(text2)):
                print('enter number only')
            else:
                return Scr

    Scr = float(getScr())

    if age >= 65 and Scr < 1:
        Scr = 1

    def getVd():
        while True:
            print('input Vd (L/hr) only: ')
            Vd = input()
            text23 = 'abcdefghijklmnopqrstuvwxyz`~:;/\|*$#^&()+=-_'
            if Vd.lower().startswith(tuple(text23)):
                print('enter number only')
            else:
                return Vd
    Vd = float(getVd())* w

    def IBW(h):
        if gender.lower().startswith('m') and h > 60:
            return 50 + 2.3*(h-60)
        elif gender.lower().startswith('m') and h <= 60:
            return 50
        elif gender.lower().startswith('f') and h > 60:
            return 45.5 + 2.3*(h-60)
        elif gender.lower().startswith('f') and h <= 60:
            return 45.5


    ibw = IBW(h)

    def getCrCl(age,gender,w):
        if ibw < w and gender.lower().startswith('m'):
            return ((140-age)*ibw)/(72*Scr)
        elif ibw < w and gender.lower().startswith('f'):
            return ((140-age)*ibw*0.85)/(72*Scr)
        elif ibw > w and gender.lower().startswith('m'):
            return ((140-age)*w)/(72*Scr)
        elif ibw > w and gender.lower().startswith('f'):
            return((140-age)*w*0.85)/(72*Scr)
    CrCl = getCrCl(age,gender,w)
    print('Your patient\'s CrCl is: ' + str(CrCl)+' (ml/min)')

    #Check to see if patient need loading dose, and calculate the loading dose
    def isSevere():
        while True:
            print('Is the infection severe? (y/n): ')
            infection = input()
            if infection in ['y','n','yes','no']:
                return infection
            else:
                print('enter \'y\' or \'n\' ')
    infection = isSevere()

    if infection.lower().startswith('y'):
        print('Infection is severe, loading dose is needed, pick loading dose from the range below')
        l1 = 20*w
        l2 = 35*w
        if l1 % 250 == 0 and l2 % 250 == 0 and l2 < 3000:
            print('minimum loading dose: '+str(l1)+ ' mg')
            print('maximum loading dose: '+str(l2)+ ' mg')
        elif l1 % 250 == 0 and l2 % 250 == 0 and l1 < 3000 < l2:
            print('minimum loading dose: '+str(l1)+ ' mg')
            print('maximum loading dose: 3000 mg')
        elif l1 % 250 == 0 and l2 % 250 == 0 and l1 > 3000:
            print('loading dose: 3000 mg')
        elif l1 % 250 == 0 and l2 % 250 != 0 and l2 < 3000:
            L2 = 250*round((l2/250)+0.5)
            print('minimum loading dose: '+str(l1) +' mg')
            print('maximum loading dose: '+str(L2)+ ' mg')
        elif l1 % 250 == 0 and l2 % 250 != 0 and l1 < 3000 < l2:
            L2 = 250*(round((l2/250)+0.5))
            print('minimum loading dose: '+str(l1)+' mg')
            print('maximum loading dose: 3000 mg')
        elif l1 % 250 == 0 and l2 % 250 != 0 and l1 > 3000:
            print('loading dose: 3000 mg ')
        elif l1 % 250 != 0 and l2  % 250 == 0 and l2 < 3000:
            L1 = 250*round((l1/250)-0.5)
            print('minimum loading dose: '+str(L1)+' mg')
            print('maximum loading dose: '+str(l2)+' mg')
        elif l1 % 250 != 0 and l2  % 250 == 0 and l1 < 3000 < l2:
            L1 = 250*round((l1/250)-0.5)
            print('the minimum loading dose: '+str(L1)+' mg')
            print('the maximum loading dose: 3000 mg')
        elif l1 % 250 != 0 and l2  % 250 == 0 and l1 > 3000:
            print('the loading dose is 3000 mg')
        elif l1 % 250 != 0 and l2 % 250 != 0 and l2 < 3000:
            L1 = 250*round(l1/250-0.5)
            L2 = 250*round(l2/250+0.5)
            print('the minimum loading dose: '+str(L1)+' mg')
            print('the maximum loading dose: '+str(L2)+' mg')
        elif l1 % 250 != 0 and l2 % 250 != 0 and l1 < 3000 < l2:
            L1 = 250 * round((l1 / 250) - 0.5)
            L2 = 250 * round((l2 / 250) + 0.5)
            print('the minimum loading dose: '+str(L1)+' mg')
            print('the maximum loading dose: 3000 mg')
        elif l1 % 250 != 0 and l2 % 250 != 0 and l1 > 3000:
            print('the loading dose is 3000 mg')
    else:
        print('the infection is not severe, no loading dose needed')

    #Calculate the dosing interval
    def getke(CrCl):
        return 0.00083*CrCl + 0.0044
    ke = getke(CrCl)

    Thalf = round((np.log(2))/ke,1)
    print('calculated dosing interval(h): '+str(Thalf)+' hr')

    if Thalf > 36:
        print('Consider intermittent/pulse dosing for vancomycin. Check patient\'s kidney function.')
    else:
        def getT():
            while True:
                print('enter your dosing interval (Q8h, Q12H, Q18H, Q24H, Q36H, Q48H) based on the calculated interval: ')
                T = input()
                if T in ['8','12','18','24','36','48']:
                    return T
                else:
                    print('enter a number from the following list: 8, 12, 18, 24, 36, 48 ')

        T = float(getT())

        #Calculate the maintenance dose
        D1 = 250*round((15*w/250)-0.5)
        D2 = 250*round((20*w/250)+0.5)
        A = []

        for i in range(D1,D2+1):
            if i % 250 == 0:
                A.append(i)
        Tinfused = []
        for i in range(len(A)):
            Tinfused.append(A[i]/1000)

        #Calculate the projected peaks/troughs for each maintenance dose
        def getCmax(x):
            return round((1000 / (ke * Vd)) * (1 - np.exp(-ke * Tinfused[x])) / (1 - np.exp(-ke * T)))
        Cmax = []
        for i in range(len(A)):
            Cmax.append(getCmax(i))

        def getCmin(x):
            return round((np.exp(-ke*(T-Tinfused[x])))*(1000/(ke*Vd))*(1-np.exp(-ke*Tinfused[x]))/(1-np.exp(-ke*T)))
        Cmin = []
        for i in range(len(A)):
            Cmin.append(getCmin(i))

        #calculate projected AUC from the regimen
        AUC = []
        for (i,j,k) in zip(Cmax,Cmin,Tinfused):   #use zip to iterate corresponding element in lists of same length
            AUC.append(round((((i-j)*k*0.5)+((i-j)/ke))*24/T))
        print('*********** Dosing parameter *************')
        print('Possible maintenance doses (mg):',A)
        print('Correspoinding peaks (µg/mL):', Cmax)
        print('Corresponding troughs (µg/mL):', Cmin)
        print('Corresponding AUCs (µg/ml.hr):', AUC)

    continue_calculation = input('Do you want to continue to calculate another dosing regimen?  ')
    if continue_calculation.lower().startswith('y'):
        continue
    else:
        break
