def is_super_ascii(s):
    freq = {}  # dictionary to count characters manually

    # Count the frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Check if each character appears as per its position in the alphabet
    for ch in freq:
        expected_count = ord(ch) - 96  # 'a' = 97 in ASCII → 97 - 96 = 1
        if freq[ch] != expected_count:
            return "No"
    return "Yes"

# 🔄 Test the function
print(is_super_ascii("abbccc"))  # ✅ Output: Yes
print(is_super_ascii("abc"))     # ❌ Output: No
