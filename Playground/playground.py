# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    """
    Strategy:
    1. Bring the origin to 'a'
        ord(letter) - ord('a')
    2. Apply the shift
        shiftedPosition = ord(letter) - ord('a') + 1
    3. Account for the case we we overflow beyond 'z' by taking the 'modulo'
        calibratedPosition = shiftedPosition % 26
    4. Bring position to real chr postion in the ascii table by applying the 'a' shift
        ans = calibratedPosition + ord('a')
    5. Finally take the chr() of the position
        return chr(ans)

    And in one line, it goes like:

    """

    return chr((((ord(letter) - ord('a') + n) % 26) + ord('a')))

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -1)
#>>> z

