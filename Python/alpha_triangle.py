# Python script to print an alpha triangle
# 
#   A B C D E F G F E D C B A
#   A B C D E F   F E D C B A
#   A B C D E       E D C B A
#   A B C D           D C B A
#   A B C               C B A
#   A B                   B A
#   A                       A
#

import string

def main():
    list1 = list(string.ascii_uppercase)[0:7]
    print('')
    for mainCntr in range(len(list1), 0, -1):
        print(*' ', end=' ')
        for cntr in range(0, len(list1), 1):
            print(*list1[cntr], sep=' ', end=' ')
        for cntr in range(len(list1)-1, 0, -1):
            print(*list1[cntr-1], sep=' ', end=' ')
        print('')
        list1[mainCntr-1] = ' '
    print('')

if __name__ == '__main__':
    main()
