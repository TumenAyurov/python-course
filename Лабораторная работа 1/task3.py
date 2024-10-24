# TODO Найдите количество книг, которое можно разместить на дискете
symbol = 4
line = symbol * 25
page = line * 50
book = page * 100
disk = 1.44 * 1024 * 1024
book_on_disk = disk // book
print("Количество книг, помещающихся на дискету:", int(book_on_disk))
