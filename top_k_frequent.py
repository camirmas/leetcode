def top_k_frequent(lst, k):
    el_map = {}

    for i in lst:
        if i in el_map:
            el_map[i] += 1
        else:
            el_map[i] = 1

    max_freq_list = []

    freq_list = [(freq, num) for num, freq in el_map.items()]
    max_freq_list = sorted(freq_list, reverse=True)

    len_maxes = len(max_freq_list)

    if k <= len_maxes:
        return [item[1] for item in max_freq_list[:k]]

    raise Exception("k must be less than the length of the input list")
