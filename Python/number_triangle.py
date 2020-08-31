# Display number triangle
#
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#

def print_num_triangle():
    num = 5
    print()
    for a in range(1, 6):
        print(' ' * (num * 2 - 1), end=' ')
        num -= 1
        for cnt in range(1, a):
            print(cnt, sep=' ', end=' ')
        for cnt in range(a, 0, -1):
            print(cnt, sep=' ', end=' ')
        print()
    print()

if __name__ == '__main__':
    print_num_triangle()
