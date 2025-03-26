encoded_segment = 'bcb4ce08a3/6317b67`d8`d58e6e1e`b'
decoded_second_part = ''.join(chr(ord(char) + 1) for char in encoded_segment)
print("Decoded Second Part:", decoded_second_part)
