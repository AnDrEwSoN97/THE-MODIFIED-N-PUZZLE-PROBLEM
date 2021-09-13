import random





def print_2_dim_array(arr):
    for i in arr:
        for j in i:
            print(i, end=" ")
        print()


def write_random_input_data(f,possible_values):
    for i in range(3):
        for j in range(3):
            index = random.randint(0, len(possible_values) - 1)
            f.write(f"{possible_values[index]} ")
            del possible_values[index]
        f.write("\n")


def main():
    for i in range(0,100):
        possible_values = [1,5,'-',2,7,4,6,3,'-']
        random.seed(i+100)
        with open(f"./goals/{i}.txt", "w") as f:
            write_random_input_data(f,possible_values)


if __name__ == '__main__':
    main()
