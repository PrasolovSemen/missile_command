from datetime import datetime
import os

def create_folders(new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    else:
        print('Folders ',new_path,' allready exist!');


def delete_folders(new_path):
    if os.path.exists(new_path):
        os.removedirs(new_path)
    else:
        print('Folders ',new_path,' allready exist!');


now = datetime.now()
year = now.year
month = now.month
PATH_DIR = 'C:\\tmp'
PATH_NEW = 'C:\\tmp'
k = 0

# for i in range(24):
#     cur_month = month - i + k
#     if (cur_month) == 0:
#         year -= 1
#         k += 12
#         cur_month = month - i + k
#
#     if cur_month < 10:
#         str_month = '0' + str(cur_month)
#     else:
#         str_month = str(cur_month)
#
#     new_path = PATH_DIR + '\\' + str(year) + '\\' + str_month
#     create_folders(new_path)

# for i in range(10,24):
#     cur_month = month - i + k
#     if (cur_month) == 0:
#         year -= 1
#         k += 12
#         cur_month = month - i + k
#
#     if cur_month < 10:
#         str_month = '0' + str(cur_month)
#     else:
#         str_month = str(cur_month)
#
#     new_path = PATH_DIR + '\\' + str(year) + '\\' + str_month
#     delete_folders(new_path)

print(os.listdir('C:\\tmp'))
list_folder_year = os.listdir('C:\\tmp')
for folder in list_folder_year:
     if int(folder) < 2018:
         new_path = 'C:\\tmp\\'+folder
         print('Delete folder ', new_path)


print('Work complete!')

