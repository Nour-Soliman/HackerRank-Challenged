def print_formatted(number):
    wid=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i).rjust(wid)
        octa=oct(i)[2:].rjust(wid)
        hexa=hex(i)[2:].upper().rjust(wid)
        bi=bin(i)[2:].rjust(wid)
        print(dec,octa,hexa,bi)
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)