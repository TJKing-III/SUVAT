import math



def suvat():
    S = input("What is the displacement? (m): (if you dont know click enter): ")
    U = input("What is the intial velocity? (ms^-1): (if you dont know click enter): ")
    V = input("What is the final velocity? (ms^-1): (if you dont know click enter): ")
    A = input("What is the acceleration? (ms^-2): (if you dont know click enter): ")
    T = input("What is the time? (Seconds): (if you dont know click enter): ")
    Equation = input("What are you trying to find out?: (S/U/V/A/T): ")
    if Equation.lower() == 's':
        if U == "":
            print((float(V)*float(T))-(0.5*float(A)*pow(float(T),2)))
        elif V == "":
            print((float(U)*float(T))+(0.5*float(A)*pow(float(T),2)))
        elif A == "":
            print(0.5*(float(V)+float(U))*float(T))
        elif T == "":
            print((pow(float(V),2) - pow(float(U),2))/(-2*float(A)))
        else:
            print("Invalid Either Give More Or Less Data")
    elif Equation.lower() == 'u':
        if S == "":
            print(float(V) - (float(A)*float(T)))
        elif V =="":
            print((float(S) - (0.5*float(A)*pow(float(T),2)))/float(T))
        elif A == "":
            print(((2*float(S))/float(T))-float(V))
        elif T == "":
            print(math.sqrt(pow(float(V),2) - (2*float(A)*float(S))))
        else:
            print("Invalid Either Give More Or Less Data")
    elif Equation.lower() == "v":
        if S == "":
            print(float(U) + (float(A) * float(T)))
        elif U == "":
            print((float(S) + (0.5*float(A)*pow(float(T),2)))/float(T))
        elif A == "":
            print(((2*float(S))/float(T))-float(U))
        elif T == "":
            print(math.sqrt((pow(float(U),2))+(2*float(A)*float(S))))
        else:
            print("Invalid Either Give More Or Less Data")
    elif Equation.lower() == "a":
        if S == "":
            print(float(V)-(float(A)*float(T)))
        elif U == "":
            print((float(S)-(float(V)*float(T))*-2)/pow(float(T),2))
        elif V == "":
            print((float(S)-(float(U)*float(T))*2)/pow(float(T),2))
        elif T == "":
            print((pow(float(V),2)-(pow(float(U),2)))/(-2*float(S)))
        else:
            print("Invalid Either Give More Or Less Data")
    elif Equation.lower() == "t":
        if S == "":
            print((float(v)-float(U))/float(T))
        elif U == "":
            Num = (pow(float(V),2))-(float(S)*2*float(A))
            if Num >= 0:
                Num = Num
            else:
                Num = -Num
                
            Num = math.sqrt(Num)
            if (float(V)+Num) > 0:
                Num = float(V)+Num
            else:
                Num = float(V)-Num
            Num = Num/float(A)
            print(Num)
        elif V == "":
            Num = (pow(float(U),2))+(float(S)*2*float(A))
            if Num >= 0:
                Num = Num
            else:
                Num = -Num
                
            Num = math.sqrt(Num)
            if (-(float(U))+Num) > 0:
                Num = -(float(U))+Num
            else:
                Num = -(float(U))-Num
            Num = Num/float(A)
            print(Num)
        elif A == "":
            print((2*float(S)/(float(U)+float(V))))
        else:
            print("Invalid Either Give More Or Less Data")
    Continue = input("Want More Equations?: (yes/no) ")
    if Continue.lower() == 'yes':
        suvat()

suvat()
