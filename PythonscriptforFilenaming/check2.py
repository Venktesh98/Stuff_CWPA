# import os

# def iter_incrementing_file_names(path):
#     """
#     Iterate incrementing file names. Start with path and add " (n)" before the
#     extension, where n starts at 1 and increases.

#     :param path: Some path
#     :return: An iterator.
#     """
#     yield path
#     prefix, ext = os.path.splitext(path)
#     for i in itertools.count(start=1, step=1):
#         yield prefix + ' ({0})'.format(i) + ext


# def safe_open(path, mode):
#     """
#     Open path, but if it already exists, add " (n)" before the extension,
#     where n is the first number found such that the file does not already
#     exist.

#     Returns an open file handle. Make sure to close!

#     :param path: Some file name.
    
#     3:return: Open file handle... be sure to close!
#     """
#     flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

#     if 'b' in mode and platform.system() == 'Windows':
#         flags |= os.O_BINARY

#     for filename in iter_incrementing_file_names(path):
#         try:
#             file_handle = os.open(filename, flags)
#         except OSError as e:
#             if e.errno == errno.EEXIST:
#                 pass
#             else:
#                 raise
#         else:
#             return os.fdopen(file_handle, mode)

# # Example
# with safe_open("some_file.txt", "w") as fh:
#     print("Hello", file=fh)

# import os

# counter = 0
# filename = "file{}.pdf"
# while os.path.isfile(filename.format(counter)):
#     counter += 1
#     print(counter)
# filename = filename.format(counter)


# def image_downloader():
    
#         image_url = 'C:\\Users\\Venktesh\\Videos\\Data\\paste.jpeg'

#         for count in range(10):
#             image_data = requests.get(image_url).content
            
#             with open(f'image_{count}.jpeg','w') as handler:
#                 handler.write(image_data)

# image_downloader()




# import os

# counter = 0
# filename = "file{}.pdf"
# while os.path.isfile(filename.format(counter)):
#     counter += 1
# filename = filename.format(counter)
# print(filename)

import os
def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
        print(path)
    with open(path,"w") as f:
        f.write("data")
        

    return path

uniquify(r'C:\Users\Venktesh\Videos\Data\file1.txt')
