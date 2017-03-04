from math import sqrt
from task3_readPDB import read_pdb_file


def get_rmsd(s1, s2):
    """
    :param s1: x,y,z coordinates of structure 1
    :type s1: tuple
    :param s2: x,y,z coordinates of structure 2
    :type s2: tuple
    :return: RMSD as float
    """
    rmsd = 0.0
    for i in range(0,len(s1)):
        rmsd = rmsd + ((s2[i][0]-s1[i][0])**2) + ((s2[i][1]-s1[i][1])**2) + ((s2[i][2]-s1[i][2])**2)
    rmsd = sqrt(rmsd/len(s1))
    return rmsd

if __name__ == '__main__':
    main_directory = 'C:\\development\\workdir\\'
    atoms1 = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '100a_lig.pdb'))
    atoms2 = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '100d_lig.pdb'))
    s1_tuple = []
    s2_tuple = []
    for atom_line in atoms1:
        if atom_line[0:4] == 'ATOM':
            coord_tuple = (float(atom_line[30:38].strip()),float(atom_line[38:46].strip()),float(atom_line[46:54].strip()))
            s1_tuple.append(coord_tuple)
    for atom_line in atoms2:
        if atom_line[0:4] == 'ATOM':
            coord_tuple = (float(atom_line[30:38].strip()), float(atom_line[38:46].strip()), float(atom_line[46:54].strip()))
            s2_tuple.append(coord_tuple)

    print(get_rmsd(s1_tuple, s2_tuple))
