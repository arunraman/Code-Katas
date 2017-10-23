def scan(para, keys):
    words = para.lower().replace('.', '').split()
    keys_pos = {x: [] for x in keys}
    win_begin = 0
    win_end = 0
    min_seg = (-1, len(words))

    for i, word in enumerate(words):
        if word not in keys_pos:
            continue
        win_end = i

        pos = keys_pos[word]
        pos.append(i)
        if len(pos) > 1 and pos[0] == win_begin:
            del pos[0]
            win_begin = min(x[0] for x in keys_pos.values() if len(x) > 0)

        if all(len(x) > 0 for x in keys_pos.values()):
            valid_seg = (win_begin, win_end)
            if valid_seg[1] - valid_seg[0] < min_seg[1] - min_seg[0]:
                min_seg = valid_seg

    if min_seg[0] == -1:
        return None
    return ' '.join(words[min_seg[0]:min_seg[1]+1])

if __name__ == '__main__':
    para = "This is a test. This is a programming test. This is a programming test in any language."
    keys = ["this", "a", "test", "programming"]
    print(scan(para, keys))