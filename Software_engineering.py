def encode(password):
    s = 3
    res = ""
    # traverse text
    for a in range(len(password)):
        checker = password[a]
        # Encrypt uppercase characters
        res += chr((ord(checker) + s - 48) % 10 + 48)

    return res


def decode(encode):
    s = 3
    res = ""
    # traverse text
    for b in range(len(encode)):
        checker = encode[b]
        # Encrypt uppercase characters
        res += chr((ord(checker) - s - 48 + 10) % 10 + 48)

    return res

if __name__ =='__main__':
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        print('Please enter an option:', end = '' )
        choice = int(input())

        if choice ==1:
            s1 = (input('Please enter your password to encode:'))
            s1Encoded = encode(s1)
            print('\n Your password has been encoded and stored!\n')
        elif choice == 2:
            s2 = s1
            s2Encoded = encode(s2)
            print(f'The encoded passsword is', s1Encoded ,'and the orginal password is', s1,'.\n')


        elif choice ==3:
            quit()
