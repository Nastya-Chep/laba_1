# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44    #Мб
count = 100
count_str = 50
count_sim = 25
one_sim = 4   #байта

volume_b = volume * 1024 * 1024

one_book_size = one_sim * count_sim * count_str * count

count_book = int(volume_b // one_book_size)

print("Количество книг, помещающихся на дискету:", count_book)
