l1 = ['disks', 'floppy', 'ssd', 'cpu']

# i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f'buy {item}')
#     i+=1
#
for index, item in enumerate(l1):  # index starts from 0
    if index % 2 == 0:
        print(f'buy {item}')
