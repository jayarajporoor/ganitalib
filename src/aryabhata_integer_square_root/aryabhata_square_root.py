#Ref - Page 199 Introduction to Indian Knowledge Systems 
two_digit_squares = [0, 1, 4,  9, 16, 25, 36, 49, 64, 81]

def find_two_digit_square(current):
    num = 0
    for m in range(len(two_digit_squares)-1, -1, -1):
        m_square = two_digit_squares[m]
        if m_square < current:
            num = m + 1
            break
        elif m_square == current:
            num = m
            break
    return num, two_digit_squares[num]

def aryabhata_integer_square_root(n, index=-1, last_quotient=-1, reminder=0, working_result=0):
    def is_varga(idx):
        return (idx % 2) == 0
    current = 0
    quotient = None
    #print("n index", n, index, "sqroot line", working_result)
    if index == -1:
        index = len(n) - 1
        if not is_varga(index):
            current = int(n[index]) * 10
            index -= 1
        current += int(n[index])
        m, m_square = find_two_digit_square(current)
        reminder = current - m_square
        quotient = m
        #print("init Q R", quotient, reminder)
    else:
        current = reminder * 10
        current += int(n[index])
        if is_varga(index):
            reminder = current - last_quotient * last_quotient
            #print("varga Q R", None, reminder)
        else:
            quotient = current // (2*working_result)
            reminder = current % (2*working_result)
            #print("avarga Q R", quotient, reminder)
    if quotient is not None:
        working_result = working_result * 10 + quotient
    if index > 0:
        return aryabhata_integer_square_root(n, index - 1, quotient, reminder, working_result)
    else:
        return working_result

def sridhara_square_root(s, p):
    s = ('0'* (2*p)) + s
    res = aryabhata_integer_square_root(s)
    return res / (10**p)

def str_reverse(s):
    return "".join(reversed(s) )     

if __name__ == "__main__":
    import sys
    import math
    n_str = str_reverse(sys.argv[1])
    if len(sys.argv) > 2:
        p = int(sys.argv[2])
    else:
        p = 3
    res0 = aryabhata_integer_square_root(n_str)
    res1 = sridhara_square_root(n_str, p=p)
    print("-----------------------")
    print( "Aryabhata integer square root:\t\t\t", res0)
    print("Sridhara's approximation for non-squares:\t", res1 )
    lib_res = math.sqrt(int(sys.argv[1]))
    print("-----------------------")
    print("Library Result Rounded:\t\t\t\t", round(lib_res))
    print("Library Result Full:\t\t\t\t", lib_res)
    print("-----------------------")
