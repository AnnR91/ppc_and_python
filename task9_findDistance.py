from math import sqrt
from task3_readPDB import read_pdb_file


def get_distance(a1, a2):
    """
    :param a1: ATOM record for atom 1
    :type a1: str
    :param a2: ATOM record for atom 2
    :type a2: str
    :return: distance as float
    """
    coord1 = (float(a1[30:38].strip()), float(a1[38:46].strip()), float(a1[46:54].strip()))
    coord2 = (float(a2[30:38].strip()), float(a2[38:46].strip()), float(a2[46:54].strip()))
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2)

if __name__ == '__main__':
    main_directory = 'C:\\development\\workdir\\'
    atoms_receptor = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '0a_rec.pdb'))
    atoms_ligand = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '0a_lig.pdb'))
    print(get_distance(atoms_receptor[0], atoms_ligand[0]))
