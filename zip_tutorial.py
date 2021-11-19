import zipfile

# my_zip = zipfile.ZipFile('zip_folder/new_files.zip','w')
# my_zip.write('zip_folder/file1.txt')
# my_zip.close()

read_zip = zipfile.ZipFile('zip_folder/new_files.zip')
for files in read_zip.namelist():
    print(files)
    print(read_zip.read(files))
read_zip.close()
