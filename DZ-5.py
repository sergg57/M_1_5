immutable_var = (3, 7, 'Яблоко', "лимон", False)
print(type(immutable_var), immutable_var)
#immutable_var[0] = 'Слон' # Кортеж - неизменяемый объект. Поэтому интерпретатор выдает ошибку
print(immutable_var[0])
mutable_list = [8, 15, 45, 'Слон', "Горилла", True]
print(type(mutable_list), mutable_list)
mutable_list[2] = 'Помидор'
print(mutable_list)