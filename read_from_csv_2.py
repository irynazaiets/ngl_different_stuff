import csv
import pickle
import re

LIST_WITH_NUMBERS_NEW = []
LIST_WITH_NUMBERS_OLD = []


with open('data/csv_files/old.csv', newline='') as old_file:
    with open('data/csv_files/new_2.csv', newline='') as new_file:

        reader_old = csv.reader(old_file)
        data_old = list(reader_old)

        reader_new = csv.reader(new_file)
        data_new = list(reader_new)


for i in data_new:
    data = re.sub(' +', ' ', i[0])
    only_numbers = re.findall(r'[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', data)
    # only_numbers = re.findall(r'\b\d+\b', data)
    if len(only_numbers)>1 and only_numbers[0].isdigit():
        if int(only_numbers[0]) in range(0, 1064, 1) and len(only_numbers)>=6:
            LIST_WITH_NUMBERS_NEW.append(only_numbers)

for i in data_old:
    data = re.sub(' +', ' ', i[0])
    only_numbers = re.findall(r'[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', data)
    # only_numbers = re.findall(r'\b\d+\b', data)
    if len(only_numbers)>1 and only_numbers[0].isdigit():
        if int(only_numbers[0]) in range(0, 1064, 1) and len(only_numbers)>=6:
            LIST_WITH_NUMBERS_OLD.append(only_numbers)

#це якась хуйня
# with open("data/list_of_numbers.csv", "w+", newline="") as file:
#     for data in LIST_WITH_NUMBERS:
#         write = csv.writer(file)
#         write.writerows(data)


dbfile_new = open('data_new.pickle', 'ab')
pickle.dump(LIST_WITH_NUMBERS_NEW, dbfile_new)                   
dbfile_new.close()

dbfile_new = open('data_new.pickle', 'rb')   
db_new = pickle.load(dbfile_new)



dbfile_old = open('data_old.pickle', 'ab')
pickle.dump(LIST_WITH_NUMBERS_OLD, dbfile_old)                   
dbfile_old.close()

dbfile_old = open('data_old.pickle', 'rb')   
db_old = pickle.load(dbfile_old)

print(len(db_new))
print(len(db_old))

# print(len(LIST_WITH_NUMBERS))
# print(LIST_WITH_NUMBERS)