# Decoding functions and XOR logic from the disassembled bytecode

def from_hex(hex_string):
    """Decode a hexadecimal string to bytes."""
    return "".join(
        chr(int(hex_string[i:i + 2], 16)) for i in range(0, len(hex_string), 2)
    )

def xor_string(input_string, key):
    """XOR decryption using a repeating key."""
    return "".join(
        chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(input_string)
    )

# Hexadecimal encoded input
hex_string = "5c404344470d1b1b445c5b45404145581a56401b766472604d"

# Decode the input string from hex
decoded_input = from_hex(hex_string)

# Search for the flag by trying keys from 0 to 999
possible_keys = [str(i) for i in range(1000)]
results = {}

for key in possible_keys:
    decrypted = xor_string(decoded_input, key)
    if "CTF{" in decrypted or "flag" in decrypted or decrypted.isprintable():
        results[key] = decrypted

# Filter results for potential URLs or web-related patterns
import pandas as pd

results_df = pd.DataFrame(results.items(), columns=["Key", "Decrypted String"])
url_patterns = ["http://", "https://", ".com", ".net", ".org", "/"]
potential_web_results = results_df[
    results_df["Decrypted String"].str.contains("|".join(url_patterns), case=False, na=False)
]

# Print results to console
print("Potential Web-Related Decryption Results:")
print(potential_web_results.to_string(index=False))
