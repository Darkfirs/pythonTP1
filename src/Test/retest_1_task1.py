import os
import sys


def merge_sequences(seq1, seq2):
    result_sequence = sorted(seq1 + seq2)
    return result_sequence


def check_file(file_in, file_out):
    if not os.path.exists(file_in):
        print(f"File '{file_in}' not found.")
        return False

    if os.path.exists(file_out):
        print(f"File '{file_out}' already exists.")
        return False
    return True


def merge_and_save(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        sequence1 = list(map(int, lines[0].split()))
        sequence2 = list(map(int, lines[1].split()))
        result_sequence = merge_sequences(sequence1, sequence2)
    with open(output_file, 'w') as file:
        file.write(' '.join(map(str, result_sequence)))
    print("Done")


def main(file1, file2):
    if check_file(file1, file2):
        merge_and_save(file1, file2)


if __name__ == "__main__":
    input_file, output_file = sys.argv[1], sys.argv[2]
    main(input_file, output_file)
