def longest_palindrome(word):
    char_map = {}

    for char in word:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    max_odd = 0
    count = 0

    for k, v in char_map.items():
        if v % 2 == 0:
            count += v
        else:
            if v > max_odd:
                if max_odd > 0:
                    count += max_odd - 1
                max_odd = v
            else:
                count += v - 1

    count += max_odd

    return count
