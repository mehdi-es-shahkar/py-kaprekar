#kapreka number 6174

def list_to_num(c):
    # take a list of numbers and return int number [7, 5, 3, 1] ---> 7531
    t = ""
    for z in c:
        t += str(z)
    return int(t)

def issamedigit(num):
    #if all all of elemnts of a list be same [3, 3, 3, 3]  this func return True else return False
    d = str(num)
    c = d[0]
    for z in  d[1: : ] :
        if z != c : return False  
    return True

def kaprekar(number, ds = [], i = 1):
    #this func return list of max num and min num and number of step that reach 6174 number
    str_number = str(number)
    ln = len(str_number)
    if  ln< 4:
        str_number = ((4 - ln) * "0" )+ str_number
    a = [ ]
    for z in str_number :
        a += [int(z)]
    a.sort()
    b = list(reversed(a))
    x = list_to_num(b)
    y = list_to_num(a)
    if x - y == 6174:
        ds += [(x, y)]
        print(f"list of couple numbers in any step is  --> {ds} ")
        ds = []
        return 
    t = x - y
    ds += [(x, y)]
    i += 1
    kaprekar(t, ds, i)


def main():
    numbers = [7531, 4400, 3155, 6666, 9172]
    for a in numbers:
        if issamedigit(a) :
            print(f"all digits of this number --> {a} is same. Please try another number")
        else:
            print(f"number is : {a} ")
            kaprekar(a, ds = [], i = 1)
            
if __name__ == "__main__":
    main()       
        

