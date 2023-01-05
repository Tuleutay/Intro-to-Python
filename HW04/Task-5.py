def parse_number(file_name):
    with open(file_name) as f:
        text_file = f.readlines()
    number_list = text_file[0].replace(' = 0', '').split(' + ')

    element_dic = {}
    for element in number_list:
        temp_element = element.split("x")
        if len(temp_element) > 1:
            number = (temp_element[0].replace("*", ""))
            odds = (temp_element[1].replace("*", ""))
            if odds == '':
                odds = 1
            if number == '':
                number = 1
            element_dic[int(odds)] = int(number)
        else:
            element_dic[0] = int(temp_element[0])
    return element_dic


def sum_numbers(first_dict, second_dict):
    first_max = (max(first_dict.keys()))
    second_max = (max(second_dict.keys()))
    results = ''
    for i in range(max(first_max, second_max), -1, -1):
        temp_number = 0
        if i in first_dict:
            temp_number += first_dict[i]
        if i in second_dict:
            temp_number += second_dict[i]
        if i == 0:
            results += '{}'.format(temp_number)
        elif i == 1:
            results += '{}*x + '.format(temp_number)
        else:
            results += '{}*x**{} + '.format(temp_number, i)
    return results


firstDict = parse_number('text1.txt')
secondDict = parse_number('text2.txt')

print(firstDict)
print(secondDict)
print(sum_numbers(firstDict, secondDict))