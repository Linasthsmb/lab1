# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, sep=','):
    new_str1 = str1.split(sep)
    new_str2 = str2.split(sep)
    set_str1 = set(new_str1)
    inter = list(set_str1.intersection(new_str2))
    return inter


# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
set2_ = find_common_participants(participants_first_group,participants_second_group)
set_ = find_common_participants(participants_first_group,participants_second_group, '|')
list_ = []
for elem in set_:
    list_.append(elem)
list_.sort()
print(list_)
