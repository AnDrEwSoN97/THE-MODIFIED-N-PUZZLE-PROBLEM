def read_data(file_name):
    temp = []
    with open(file_name) as f:
        for i in f.readlines():
            temp.append(i.strip().split())
    return temp