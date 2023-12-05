from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')

# Добавляем факты о родительских связях
+ parent('Мария', 'Иван') # Мария является родителем Ивана
+ parent('Иван', 'Сергей') # Иван является родителем Сергея

# Определяем правило для нахождения дедушек и бабушек
# X является дедушкой или бабушкой Y, если X является родителем Z, и Z в свою очередь является родителем Y
grandparent(X, Y) <= parent(X, Z) & parent(Z, Y)

# Делаем запрос, чтобы найти всех дедушек и бабушек Сергея
print(grandparent(X, 'Сергей')) # Выводит Марию, так как Мария является родителем Ивана, а Иван - родителем Сергея