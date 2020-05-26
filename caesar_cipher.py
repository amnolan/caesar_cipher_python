## caesar.py

# checks upper case
def is_upper(char):
	return 'A' <= char and char <= 'Z'

# checks lower case
def is_lower(char):
	return 'a' <= char and char <= 'z'

# encodes an upper case char
def encode_upper(char, shift):
	return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

# encodes a lower case char
def encode_lower(char, shift):
	return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

# main encoding method
def encode(msg, shift):
    
    newmsg = ""
    msg_ra = list(msg)

    # for each character in the string
    for ch in msg:
        # next character to be assigned
        new_curr_char = ''
        # check if upper, lower or none
        if (is_upper(ch)):
            new_curr_char = encode_upper(ch, shift)
        elif (is_lower(ch)): 
            new_curr_char = encode_lower(ch, shift)
        else:
            new_curr_char = ch
        # incrementally grow the string each iteration until complete
        newmsg = newmsg + new_curr_char
    return newmsg

msg = input("Enter message to be encrypted: ")
shiftstr = input("Enter shift amount (1-25): ")
shift = int(shiftstr) 

print("Encrypted message: " + encode(msg, shift))
