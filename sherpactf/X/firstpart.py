expected_values = [56, 61, 38, 60, 50, 91, 91, 12]
xor_values = [0x6B, 0x75, 0x65, 0x68, 0x74, 0x69, 0x6F, 0x77]

decoded_first_part = [chr(expected ^ xor) for expected, xor in zip(expected_values, xor_values)]
print("".join(decoded_first_part))  # This gives the first 8 characters of the flag.
