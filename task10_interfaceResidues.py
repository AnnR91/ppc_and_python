from task3_readPDB import read_pdb_file
from task9_findDistance import get_distance


def get_interface_residues(atoms1, atoms2):
    """
    :param atoms1: ATOM records list for atom 1
    :type atoms1: list
    :param atoms2: ATOM records list for atom 2
    :type atoms2: list
    :return: interface residues as a list
    """
    interface = []
    for a1 in atoms1:
        for a2 in atoms2:
            distance = get_distance(a1, a2)
            if distance <= 10.0:
                interaction = '%s WITH %s' % (a1[17:26], a2[17:26])
                if interaction not in interface:
                    interface.append(interaction)
    return interface

if __name__ == '__main__':
    main_directory = 'C:\\development\\workdir\\'
    atoms_receptor = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '0a_rec.pdb'))
    atoms_ligand = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '0a_lig.pdb'))
    print(get_interface_residues(atoms_receptor, atoms_ligand))
