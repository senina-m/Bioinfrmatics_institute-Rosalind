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
            my_dict[seq_name] = fasta
            fasta = ""
            seq_name = "".join(arr[1:])
        else:
            fasta = fasta + "".join(arr[0:])
    f.close()
    my_dict[seq_name] = fasta
    my_dict.pop("start")
    return my_dict


def count_cg(sequence):
    seq_arr = list(sequence)
    cg = 0
    for letter in seq_arr:
        if letter == "C" or letter == "G":
            cg = cg + 1

    if len(seq_arr) == 0:
        return 0
    else:
        return cg / len(seq_arr) * 100


dictionary = read("rosalind_gc.txt")
max_num = 0
max_name = ""
for key in dictionary.keys():
    seq = dictionary.get(key)
    num = count_cg(seq)
    if max_num < num:
        max_num = num
        max_name = key
print(max_name)
print(max_num)
