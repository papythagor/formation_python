nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs2 = []

nombres_pairs2 = [i for i in nombres if i % 2 == 0]
print(nombres_pairs2)

print("---")
# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs2 = []

nombres_positifs2 = [i for i in nombres if i>=0]
print(nombres_positifs2)
# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles2 = []

nombres_doubles2 = [i * 2 for i in nombres]
print(nombres_doubles2)
# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses2 = []


nombres_inverses2 = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses2)