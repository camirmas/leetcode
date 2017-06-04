def find_anagrams(s, p):
    start_i = 0
    curr_i = 0
    indices = []
    count = len(p)

    p_map = {}

    for char in p:
        if char in p_map:
            p_map[char] += 1
        else:
            p_map[char] = 1

    while curr_i < len(s):
        if s[curr_i] in p_map:
            p_map[s[curr_i]] -= 1
            if p_map[s[curr_i]] >= 0:
                count -= 1

        if count == 0:
            indices.append(start_i)

        if curr_i == start_i + len(p) - 1:
            if s[start_i] in p_map:
                if p_map[s[start_i]] >= 0:
                    count += 1
                p_map[s[start_i]] += 1
            start_i += 1
        curr_i += 1


    return indices
