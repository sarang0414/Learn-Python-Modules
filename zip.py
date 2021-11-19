import sys
import zipfile

def my_zip(zip_dir,file1,file2):
    z1 = zipfile.ZipFile(zip_dir,'w')
    z1.write(file1)
    z1.write(file2)
    z1.close()

    z2 = zipfile.ZipFile(zip_dir)
    for files in z2.namelist():
        print(files)
        print(z2.read(files))
    z2.close()

my_zip(sys.argv[1],sys.argv[2],sys.argv[3])