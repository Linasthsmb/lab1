# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
count_of_pages = 100
count_of_strings = 50
num = 25
vol_for_one = 4
one_book = count_of_pages*count_of_strings*num*vol_for_one/1024/1024
maximum = int(volume//one_book)

print("Количество книг, помещающихся на дискету:", maximum)
