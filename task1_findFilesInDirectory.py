import os

directory = 'C:\\development\\sources\\1KXP_dockedPoses'
# directory = os.path.normpath('C:/development/sources/1KXP_dockedPoses')

list_of_files = os.listdir(directory)
print(list_of_files)

output = open('%s\\filelist.txt' % directory,'w')
for file in list_of_files:
    if 'pdb' in file:
        output.write('%s\n' % file)
output.close()
