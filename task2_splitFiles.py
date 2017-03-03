import os

main_directory = 'C:\\development'
receptor_chains = ['A']
ligand_chains = ['B']

input_file = open('%s\\sources\\1KXP_dockedPoses\\filelist.txt' % main_directory).readlines()
os.system('mkdir %s\\workdir\\afterSplit' % main_directory)
for file_name in input_file:
    file_name = file_name.strip()
    # if file_name != '0a.pdb':
    #     break
    pdb_file = open('%s\\sources\\1KXP_dockedPoses\\%s' % (main_directory, file_name))
    receptor_file_name = '%s_rec.pdb' % file_name[0:-4]
    ligand_file_name = '%s_lig.pdb' % file_name[0:-4]
    receptor_file = open('%s\\workdir\\afterSplit\\%s' % (main_directory, receptor_file_name), 'w')
    ligand_file = open('%s\\workdir\\afterSplit\\%s' % (main_directory, ligand_file_name), 'w')
    for line in pdb_file:
        if line[0:4] == 'ATOM' and line[21] in receptor_chains:
            receptor_file.write(line)
        elif line[0:4] == 'ATOM' and line[21] in ligand_chains:
            ligand_file.write(line)
    receptor_file.write('TER\n')
    receptor_file.close()
    ligand_file.write('TER\n')
    ligand_file.close()