#function to print binary values of various input like integer,char,also perform shift operation on integer

def binary(num:int):
    no_of_bits=num.bit_length()
    print(no_of_bits)
    mask=1
    mask=mask<<no_of_bits-1
    for _ in range(no_of_bits):
        if(num & mask):
            print("1",end="")
        else:
            print("0",end="")
        mask=mask>>1
    print("\n")
    print(bin(10))
    


input=int((input("Enter a number:")))
binary(input)