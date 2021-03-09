def read(filename):
    my_dict = {}
    f = open(filename, "r")
    seq_name = "start"
    fasta = ""
    for line in f:
        arr = list(line)
        if arr[len(arr) - 1] == "\n":
            arr = arr[0:-1]
        if arr[0] == ">":
            my_dict[seq_name] = list(fasta)
            fasta = ""
            seq_name = "".join(arr[1:])
        else:
            fasta = fasta + "".join(arr[0:])
    f.close()
    my_dict[seq_name] = list(fasta)
    my_dict.pop("start")
    return my_dict


def sequential_slice(iterable, length):
    pool = tuple(iterable)
    assert 0 < length <= len(pool)
    tails = (pool[s:] for s in range(length))  # Срезы не ленивы?
    return zip(*tails)


def sequence_in_list(sequence, lst):
    pool = tuple(sequence)
    return any((pool == s for s in sequential_slice(lst, len(pool))))


def lcs(a, b):
    if len(a) > len(b):
        a, b = b, a
    for l in reversed(range(1, len(a) + 1)):
        seq = [subseq for subseq in sequential_slice(a, l) if sequence_in_list(subseq, b)]
        if seq:
            break
    return seq


sequences = read("test.txt")
for line1 in sequences.values():
    for line2 in sequences.values():
        if line1 != line2:
            line = lcs(line1, line2)
