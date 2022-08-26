import numpy as np
# will try to code using system of equation
def num_validation(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print('Enter a number only!!!')
            continue
        if value < 0:
            print('Enter a positive number only!!')
            continue
        else:
            break
    return value

desired = num_validation('Enter the desired concentration/percentage: ')
def get_smaller():
    while True:
        smaller = num_validation('Enter the smaller stock concentration/percentage (enter 0 if you are adding pure diluent): ')
        if smaller >= desired:
            print('this number must be smaller than the desired concentration/percentage!!! ')
        else:
            return smaller
smaller = get_smaller()

def get_bigger():
    while True:
        bigger = num_validation('Enter the bigger stock concentration/percentage (enter 100 if you are adding pure API): ')
        if bigger <= desired:
            print('this number must be bigger than the desired concentration/percentage!!! ')
        else:
            return bigger
bigger = get_bigger()

def availability_of_amount():
    while True:
        print('''Which of the following amount (mg, ml, etc..) is available (smaller stock concentration/percentage, bigger stock concentration/percentage, or desired concentration/percentage)?
        Enter "s" if the smaller stock concentration/percentage amount is given 
        Enter "b" if the bigger stock concentration/percentage amount is given 
        Enter "d" if the desired concentration/percentage amount is given''')
        a = input()
        if a not in ['s','b','d']:
            print('Enter "s", "b", or "d" only !!! ')
        else:
            return a
a = availability_of_amount()

#solve the equation
if a == 's':
    s = num_validation('Enter the smaller stock concentration amount: ')
    A = np.array([[1,0],[smaller-desired,bigger-desired]])
    B = np.array([s,0])
    X = np.linalg.solve(A,B)
    print('The bigger stock concentration amount: '+ str(X[1]))
    print('The total amount of desired concentration: '+ str(s+X[1]))
if a == 'b':
    b = num_validation('Enter the bigger stock concentration amount: ')
    A = np.array([[0, 1], [smaller-desired, bigger-desired]])
    B = np.array([b, 0])
    X = np.linalg.solve(A, B)
    print('The smaller stock concentration amount: ' + str(X[0]))
    print('The total amount of desired concentration: ' + str(b + X[0]))
if a == 'd':
    d = num_validation('Enter the desired stock concentration amount: ')
    A = np.array([[1, 1], [smaller-desired, bigger-desired]])
    B = np.array([d, 0])
    X = np.linalg.solve(A, B)
    print('The bigger stock concentration amount: ' + str(X[1]))
    print('The smaller concentration amount: ' + str(X[0]))


