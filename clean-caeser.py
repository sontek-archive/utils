#!/usr/bin/python
from string import letters, maketrans

def decode(input, shift):
    return modify_input(input, -shift)

def encode(input, shift):
    return modify_input(input, shift)

def modify_input(input, shift):
    trans = maketrans(letters, letters[shift:] + letters[:shift])
    return input.translate(trans)

def get_shift():
    try:
        shift = int(raw_input('What shift would you like to use?\n'))
    except ValueError:
        print 'Shift must be a number'
        shift = get_shift()

    if not (shift > 0 and shift <= 25):
        print 'Shift must be between 1 and 25'
        shift = get_shift()

    return shift

def main():
    try:
        task = int(raw_input('1) Encode \n'+ \
                             '2) Decode \n'))
    except ValueError:
        print 'Invalid task, try again!'
        main()

    shift = get_shift()
    input = raw_input('What message would you like to %s\n' % ('Encode' if task == 1 else 'Decode'))

    if task == 1:
        print encode(input, shift)
    elif task == 2:
        print decode(input, shift)

if __name__ == '__main__':
    main()
