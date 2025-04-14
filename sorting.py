import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {}
    with open(file_path, "r", encoding = "utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key, value in row.items():
                if key not in data:
                    data[key] = []

                number = int (value)
                data[key].append(number)
    return data

def selection_sort(sequence, direction):
    for idx in range(len(sequence)):
        min_idx = idx
        for idx_new in range(idx + 1, len(sequence)):

            if direction == "ascend":
                if sequence[idx_new] < sequence[min_idx]:
                    min_idx = idx_new
            else:
                if sequence[idx_new] > sequence[min_idx]:
                   min_idx = idx_new

        sequence[idx] , sequence[min_idx] = sequence[min_idx],  sequence[idx]

    return sequence

def bubble_sort(sequence):
    for idx in range(len(sequence) - 1):
        for idx_new in range(len(sequence) - idx - 1):
            if sequence[idx_new] > sequence[idx_new + 1]:
                sequence[idx_new + 1], sequence[idx_new] =  sequence[idx_new], sequence[idx_new + 1]

    return sequence

def insertion_sort(sequence):
    for idx in range (1, len(sequence)):
        value = sequence[idx]
        j = idx - 1
        while sequence[j] > value and (j >= 0):
            sequence[j + 1] , sequence[j] = sequence[j] , sequence[j+1]
        sequence[j + 1] = value

    return sequence








def main():
    my_data = read_data("numbers.csv")
    print(my_data)

    selekce = selection_sort(my_data["series_1"], "des")
    print(selekce)

    bubble = bubble_sort(my_data["series_1"])
    print(bubble)

    insertion = insertion_sort(my_data["series_1"])
    print(insertion)

if __name__ == '__main__':
    main()
