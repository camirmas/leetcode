def intersection(nums1, nums2):
    n1_map = {}
    n2_map = {}

    for n in nums1:
        if n in n1_map:
            n1_map[n] += 1
        else:
            n1_map[n] = 1

    for n in nums2:
        if n in n2_map:
            n2_map[n] += 1
        else:
            n2_map[n] = 1

    res = []

    for k, n1_v in n1_map.items():
        if k in n2_map:
            n2_v = n2_map[k]
            v_final = min(n1_v, n2_v)
            to_add = [k] * v_final
            res.extend(to_add)

    return res
