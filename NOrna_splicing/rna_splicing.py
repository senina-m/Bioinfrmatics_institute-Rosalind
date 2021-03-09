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


my_dict = read("test.txt")
line = list(list(my_dict.values())[0])
substrings = list(my_dict.values())[1:]
