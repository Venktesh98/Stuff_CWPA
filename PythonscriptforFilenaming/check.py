# import os

# file_name = "file_name.txt"
# if os.path.isfile(file_name):
#     expand = 1
#     while True:
#         expand += 1
#         new_file_name = file_name.split(".txt")[0] + str(expand) + ".txt"
#         if os.path.isfile(new_file_name):
#             continue
#         else:
#             file_name = new_file_name
#             break


import tempfile
import itertools as IT
import os

def uniquify(path, sep = ''):
    def name_sequence():
        count = IT.count()
        yield ''
        while True:
            yield '{s}{n:d}'.format(s = sep, n = next(count))
    orig = tempfile._name_sequence 
    with tempfile._once_lock:
        tempfile._name_sequence = name_sequence()
        path = os.path.normpath(path)
        dirname, basename = os.path.split(path)
        filename, ext = os.path.splitext(basename)
        fd, filename = tempfile.mkstemp(dir = dirname, prefix = filename, suffix = ext)
        tempfile._name_sequence = orig
    return filename

print(uniquify('/Data/file.pdf'))
