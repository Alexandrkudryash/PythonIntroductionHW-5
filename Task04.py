# Домашнее задание 5.
# Задача 4.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

####начало ######решение от преподавателя######################
# def coding(txt):
#    count = 1
#    res = ''
#    for i in range(len(txt)-1):
#     if txt[i] == txt[i+1]:
#        count += 1
#     else:
#        res = res + str(count) + txt[i]
#        count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#        res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     num = ''
#     res = ''
#     for i in range(len(txt)):
#        if not txt[i].isalpha():
#           num += txt[i]
#        else:
#           res = res + txt[i] * int(num)
#           num = ''
#     return res

#####конец #####решение от преподавателя######################

####начало ######решение от Аббос Атамуратов - код не работает ######################

# def Squash(inp_text):
#   result = []
#   i=0
#   while i in range(len(inp_text) - 1):
#     counter = 1
#     key = inp_text[i]
#     for j in range(i + 1, len(inp_text)):
#        if key == inp_text[j]:
#           counter += 1
#        else:
#         i += counter
#     if counter == 1:
#      result.append((key, 1))
#     else:
#      result.append((key, counter))
#     break
#     result.append((inp_text[-1], 1))
#     return result

# def Unpack (inp_list):
#     result=''
#     for i in inp_list:
#       result = result + i[0]*i[1]
#       return result

# text = input('Введите строку: ')
# a = Squash(text)
# print(a)
# print (Unpack(a))

#####конец #####решение от Аббос Атамуратов######################

def encode(string: str):
    res = []
    len_ = len(list(string))
    count = 1
    for i in range(len_):
        if i < len_ - 1:
            if string[i] == string[i+1] and count < 9:
                count += 1
                continue
            else:
                res.append(f"{count}{string[i]}")
                count = 1
                continue
        else:
            res.append(f"{count}{string[i]}")
            break
    return "".join(res)


def decode(string: str):
    res = []
    l = len(string)
    for i in range(1, l, 2):
        res.append(string[i] * int(string[i - 1]))
    return "".join(res)

print(encode('ааавввввгдддд'))
print(decode(encode('ааавввввгдддд')))
