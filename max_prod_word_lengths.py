def words_intersect(w1, w2):
    w1 = set(list(w1))
    w2 = set(list(w2))

    for char in w1:
        if char in w2:
            return True
    return False

def max_product_word_lengths(words):
    max_p = 0

    for w1 in words:
        for w2 in words:
            if not words_intersect(w1, w2):
                prod = len(w1) * len(w2)
                max_p = max(max_p, prod)

    return max_p
