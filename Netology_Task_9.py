import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# TODO 1: печать списка новостроек с их порядковыми номерами
new_flats = list()
for i, flat in enumerate(flats_list):
    if 'новостройка' in flat:
        new_flats.append(flat)
        print("Порядковый номер {}:  {}".format(i + 1, flat))

# # TODO2: Сравнение 3-х новостроек друг с другом
count_new_flats = 0
how_much = 3
len_new_flats = len(new_flats) - how_much

while count_new_flats < len_new_flats:
    flats_intersection = set(new_flats[count_new_flats]) & set(
        set(new_flats[count_new_flats + 1]) & set(new_flats[count_new_flats + 2]))
    count_new_flats += 1
    print('Сравнение новостроек {}, {}, {}:'.format(count_new_flats, count_new_flats + 1, count_new_flats + 2),
          flats_intersection)

# # TODO3: работа со словарем
test_dict = dict()
for i, flat in enumerate(flats_list):
    if i == 0:
        continue
    test_dict[flat[len(flat) - 1]] = flat[0]
print(test_dict)