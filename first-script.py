def main():
    hello = 1
    hello = 2
    print(hello)


def favourite_fruit():
    my_favourite_fruit = 'banana'
    user_favourite_fruit = input('What is your favourite fruit? ')
    if not(user_favourite_fruit == my_favourite_fruit):
        print(f'{user_favourite_fruit} is not so great compared to {my_favourite_fruit}')
    else:
        print('Great choice!')

def print_all_nums_to(to):
    for i in range(to + 1):
        if not(bool(i)):
            continue
        elif i>=to:
            break
        print(i)

if __name__ == '__main__':
    main()

