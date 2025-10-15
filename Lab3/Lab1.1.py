def create_file_f1():
    with open("F1.txt", "w", encoding="utf-8") as file:
        while (line := input()) != "":
            file.write(line + "\n")


def copy_lines_n_to_k(name_file1, name_file2):
    n, k = int(input("First line: ")), int(input("Second line: "))

    with open(name_file1, "r", encoding="utf-8") as f1:
        lines = f1.readlines()

    if n > k or n < 1 or k > len(lines):
        print("Ошибка в диапазоне строк")
        return

    with open(name_file2, "w", encoding="utf-8") as f2:
        f2.writelines(lines[n - 1:k])


def count_consonants_in_f2():
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"

    with open("F2.txt", "r", encoding="utf-8") as file:
        consonant_count = sum(1 for char in file.read().lower() if char in consonants)

    print(f"Согласных в F2: {consonant_count}")


create_file_f1()
copy_lines_n_to_k("F1.txt", "F2.txt")
count_consonants_in_f2()