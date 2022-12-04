# Check which file is missing
from os.path import exists

unformated = 'KH.2007.01.%s.PDF'
offset = 1
start = 153
stop = 299

for i in range(1, 300):
    if not exists(unformated % format(i, '03d')):
        print(i)
