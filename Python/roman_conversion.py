# Given a number in decimal form convert and print it's Roman Numerical Form
# Program demands number less than 1000 because, its difficult to represent,
# 5000 as a bar on top of V in terminal/Rather I have no idea how to represent ;).

roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def getRomanForm(num):
    if num <= 1000:
        roman_num = []
        while num != 0:
            for key in roman_dict:
                if num >= key:
                    roman_num.append(roman_dict[key])
                    num -= key
                    break
        return "".join(roman_num)
    else:
        return "Please enter a number less than 1000! ..."

if __name__ == '__main__':
    print()
    print("# This program prints Roman numerical form of a decimal number(<= 1000)")
    print()
    print("Roman equivalent: {}".format(getRomanForm(int(input("Enter a number: ")))))
    print()
