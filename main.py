import random

# 1 ================================================

# def generator():
#     for i in range(50):
#         if i%2==0:
#             yield i

# for i in generator():
#     print(i)

# 2 ================================================

# def alf():
#     for i in range(65,91):
#         yield i

# for i in alf():
#     print(chr(i))

# 3 ========================================


# @staticmethod
# def fu():
#     random_len = random.randint(1,12) #длина слова
#     random_arr = [chr(random.randint(65, 91)) for _ in range(random_len)] #конверт цифр в буквы алфавита и добавление в список
#     random_str = ''.join(str(element) for element in random_arr)  #конверт списка в строку
#     return random_str
        
# random_str = fu()
# print(random_str)