import numpy as np

# Weight and CrCl calculation
def num_validation(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print('Enter number only!!!')
            continue
        if value <= 0:
            print('This is not a valid number, enter positive number only')
            continue
        else:
            break
    return value

def getGender():
    while True:
        print('Enter patient\'s gender: ')
        gender = input()
        if gender not in ['male','female','m','f']:
            print('Enter a valid gender (male, female, m, f)')
        else:
            return gender
gender = getGender()

def getIBW():
    h = num_validation('Enter patient\'s height (inch only): ')
    if gender.lower().startswith('m'):
        return 50 + 2.3 *(h-60) if h > 60 else 50
    if gender.lower().startswith('f'):
        return 45.5 + 2.3*(h-60) if h > 60 else 45.5
IBW = getIBW()

actual_body_weight = num_validation('Enter patient\'s weight (kg only): ')

def getAdj():
    return 0.6 * IBW + 0.4 * actual_body_weight
adjust_body_weight = getAdj()
age = num_validation('Enter patient\'s age: ')
SCr = num_validation('Enter patient\'s serum creatinine (mg/dL): ')
if age >= 65 and SCr < 1:
    SCr = 1
def getCrCl():
    if gender.lower().startswith('m') and IBW < actual_body_weight:
        return ((140-age) * IBW)/(72*SCr)
    if gender.lower().startswith('m') and IBW > actual_body_weight:
        return ((140-age) * actual_body_weight)/(72*SCr)
    if gender.lower().startswith('f') and IBW < actual_body_weight:
        return ((140-age) * IBW * 0.85)/(72*SCr)
    if gender.lower().startswith('f') and IBW > actual_body_weight:
        return ((140-age) * actual_body_weight * 0.85)/(72*SCr)
CrCl = round(getCrCl())
print('Patient\'s estimated CrCl using Cockcroft Gault\'s equation: '+ str(CrCl) + ' ml/min')

# Dosing and kinetic parameter

while True:
    def dosing_strategies():
        while True:
            print('Enter dosing strategies --> extended interval dosing ("EID") or "plazomicin" ')
            dosing = input()
            if dosing not in ['EID','plazomicin']:
                print('Enter either "EID" or "plazomicin" only!!! ')
            else:
                return dosing
    dosing = dosing_strategies()
    if dosing == 'EID' and CrCl >= 30:
        dose = 0
        def dosing_weight_extend_interval():
            if actual_body_weight > 1.2 * IBW:
                return adjust_body_weight
            else:
                return actual_body_weight
        dosing_weight_EID = dosing_weight_extend_interval()

        def getAbx():
            while True:
                abx = input('''*** Enter your chosen antibiotic for EID *** 
                    Enter "gen" for gentamicin
                    Enter "tobra" for tobramycin
                    Enter "ami" for amikacin:   
                    ''')
                if abx in ['gen', 'tobra', 'ami']:
                    return abx
                else:
                    print('Enter "gen", "tobra", or "ami" only !!!')
        abx = getAbx()

        if abx == 'gen' or abx == 'tobra':
            dose = 7 * dosing_weight_EID
        if abx == 'ami':
            def infection_ami():
                while True:
                    infection = input('Is this a ventilator associated infection (VAP) (y/n)? ')
                    if infection not in ['y', 'n']:
                        print('Enter "y" or "n" only !!')
                    else:
                        return infection
            infection = infection_ami()
            if infection == 'y':
                dose = 20 * dosing_weight_EID
            else:
                dose = 15 * dosing_weight_EID
        def get_dosing_interval_EID():
            if CrCl >= 60:
                return 24
            if CrCl >= 40 and CrCl < 60:
                return 36
            else:
                return 48
        T = get_dosing_interval_EID()
        print('***** Dosing regimen for EID *****')
        print('The dose of ' + abx + ' is: ' + str(dose) + ' mg Q' + str(T) + 'H')
        print('The above interval and dose is initial dosing regimen. Adjust accordingly using Hartford Nomogram 6-14 hrs after the first dose')
    if dosing == 'EID' and CrCl < 30:
        print('This patient\'s CrCl is less than 30, hence only qualified for traditional dosing - TD')
        def getAbx():
            while True:
                abx = input('''*** Enter your chosen antibiotic for TD *** 
                    Enter "gen" for gentamicin
                    Enter "tobra" for tobramycin
                    Enter "ami" for amikacin:   
                    ''')
                if abx not in ['gen', 'ami', 'tobra']:
                    print('Enter "gen", "tobra", or "ami" only !!!')
                else:
                    return abx
        abx = getAbx()
        trough = 1
        def condition():
            while True:
                condition = input('Enter patient\'s condition ("pneumonia", "bacteremia", "cystic fibrosis", "GI infection, "gynecology infection", "UTI", or "synergy"): ')
                if condition in ['pneumonia','bacteremia','cystic fibrosis','GI infection','gynecology infection','UTI','synergy']:
                    if abx == 'gen' and condition == 'pneumonia' or condition == 'bacteremia' or condition == 'GI infection' or condition == 'gynecology infection':
                        return 8
                    elif abx == 'tobra' and condition == 'pneumonia' or condition == 'bacteremia' or condition == 'GI infection' or condition == 'gynecology infection':
                        return 8
                    elif abx == 'gen' and condition == 'UTI':
                        return 6
                    elif abx == 'tobra' and condition == 'UTI':
                        return 6
                    elif abx == 'gen' and condition == 'synergy':
                        return 4
                    elif abx == 'tobra' and condition == 'synergy':
                        return 4
                    elif abx == 'ami':
                        return 30
                else:
                    print('Enter a condition from the list above only')
        peak = condition()
        def dosing_weight_traditional():
            if actual_body_weight < IBW:
                return actual_body_weight
            if actual_body_weight > IBW and actual_body_weight <= 1.2* IBW:
                return IBW
            else:
                return adjust_body_weight
        dosing_weight_TD = dosing_weight_traditional()
        ke = 0.00285 * CrCl + 0.015
        Vd = 0.25 * dosing_weight_TD
        interval_TD = (np.log(peak/trough))/ke + 0.5
        print('Estimated interval: '+ str(interval_TD))
        def getT():
            while True:
                interval = input('round and enter the above interval to the following --> "8" for Q8h, "12" for Q12h, "18" for 18h, "24" for 24h: ')
                if interval in ['8','12','18','24']:
                    return interval
                else:
                    print('Enter "8", "12", "18, "24" only !!')
        interval_TD_1 = int(getT())
        dose_TD = round(peak * Vd * (1-np.exp(-ke*interval_TD_1))/5) * 5
        print('***** Traditional dosing regimen is below *****!!!')
        print(abx + ': ' + str(dose_TD) + ' mg Q' + str(interval_TD_1) + 'H')
    if dosing == 'plazomicin':
        print('***** plazomicin regimen *****')
        def CrCl_plazo():
            if actual_body_weight >= 1.25 * IBW and gender.lower().startswith('m'):
                return ((140-age) * IBW)/(72*SCr)
            if actual_body_weight < 1.25 * IBW and gender.lower().startswith('m'):
                return ((140-age) * actual_body_weight)/(72*SCr)
            if actual_body_weight >= 1.25 * IBW and gender.lower().startswith('f'):
                return ((140-age) * IBW * 0.85)/(72*SCr)
            if actual_body_weight < 1.25 * IBW and gender.lower().startswith('f'):
                return ((140-age) * actual_body_weight * 0.85)/(72*SCr)
        CrCl_plazo = CrCl_plazo()
        def dose_plazo():
            plazo = 0
            if CrCl_plazo >= 60:
                if actual_body_weight < 1.25 * IBW:
                    plazo = 15 * actual_body_weight
                if actual_body_weight >= 1.25 * IBW:
                    plazo = 15 * IBW
                print('plazomicin: '+ str(plazo)+ ' mg Q24H')
            if CrCl_plazo < 60 and CrCl_plazo >= 30:
                if actual_body_weight < 1.25 * IBW:
                    plazo = 10 * actual_body_weight
                if actual_body_weight >= 1.25 * IBW:
                    plazo = 10 * IBW
                print('plazomicin: ' + str(plazo) + ' mg Q24H')
            if CrCl_plazo < 30 and CrCl_plazo >= 15:
                if actual_body_weight < 1.25 * IBW:
                    plazo = 10 * actual_body_weight
                if actual_body_weight >= 1.25 * IBW:
                    plazo = 10 * IBW
                print('plazomicin: ' + str(plazo) + ' mg Q48H')
            if CrCl_plazo < 15:
                print('actually DO NOT use plazomicin since there was no studies on that renal function')
        dose_plazo()
    calculation_continue = input('Do you want to continue to calculate another aminoglycoside regimen (y/n)? ')
    if calculation_continue.lower().startswith('y'):
        continue
    else:
        break













































