def valid_anagram(s1, s2):
    count = len(s2)
    s_map = {}

    if len(s1) != len(s2):
        return False

    for char in s1:
        if char in s_map:
            s_map[char] += 1
        else:
            s_map[char] = 1

    for char in s2:
        if char in s_map:
            if s_map[char] > 0:
                s_map[char] -= 1
                count -= 1
            else:
                return False
        else:
            return False

    return count == 0
