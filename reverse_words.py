def reverse(sent, start, end):
    sent = list(sent)

    while start < end:
        sent[start], sent[end] = sent[end], sent[start]
        start += 1
        end -= 1

    return sent

def reverse_words(sent):
    wd_start = 0
    wd_end = 0

    while wd_end < len(sent):
        if sent[wd_end] == ' ':
            sent = reverse(sent, wd_start, wd_end - 1)
            wd_end += 1
            wd_start = wd_end
        else:
            wd_end += 1

    sent = reverse(sent, wd_start, wd_end - 1)

    return ''.join(sent)
