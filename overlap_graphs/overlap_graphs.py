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


result = []
strings = read("rosalind_grph.txt")
for key1 in strings.keys():
    for key2 in strings.keys():
        if strings[key1][:3] == strings[key2][-3:] and key1 != key2:
            result.append(key2 + " " + key1)
for line in result:
    print(line)
