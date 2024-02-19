str1 = "aabbcc"
str2 = "abbcc"

def common_characters(str1, str2):
    # Перетворення до нижнього регістру
    str1_lower = str1.lower()
    str2_lower = str2.lower()

    # кількість букв в обох рядках
    count_dict_str1 = {}
    count_dict_str2 = {}

    # Скільки букв в першому рядку
    for char in str1_lower:
        count_dict_str1[char] = count_dict_str1.get(char, 0) + 1

    # скільки букв в 2 рядку
    for char in str2_lower:
        count_dict_str2[char] = count_dict_str2.get(char, 0) + 1

    # Спільні букви в двох рядках
    common_chars = set(count_dict_str1.keys()) & set(count_dict_str2.keys())


    common_chars = [char for char in common_chars if count_dict_str1[char] == count_dict_str2[char]]

    # за алфавітом
    common_chars.sort()

    return common_chars

result_example = common_characters(str1, str2)
print(result_example)

