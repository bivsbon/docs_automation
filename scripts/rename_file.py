import os

unformated = 'KH.2007.01.%s.PDF'
offset = 1
start = 153
stop = 299

for i in reversed(range(start, stop + offset)):
    os.rename(unformated
              % format(i, '03d'), unformated % format(i+offset, '03d'))