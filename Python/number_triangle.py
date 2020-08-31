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
        print(*[i for i in range(1, a+1)], sep=' ', end=' ')
        print(*[i for i in range(a-1, 0, -1)], sep=' ', end=' ')
        print()
        num -= 1
    print()

if __name__ == '__main__':
    print_num_triangle()
