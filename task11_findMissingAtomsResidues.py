from task3_readPDB import read_pdb_file
from task9_findDistance import get_distance


def get_residue_contents(res):
    residue = {}
    residue['GLY'] = ['4', ' N  ', ' CA ', ' C  ', ' O  ']
    residue['ALA'] = ['5', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ']
    residue['LEU'] = ['8', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2']
    residue['ILE'] = ['8', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG1', ' CG2', ' CD1']  # CD in CHARMM means CD1 in PDB file
    residue['VAL'] = ['7', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG1', ' CG2']
    residue['ASP'] = ['8', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' OD1', ' OD2']
    residue['GLU'] = ['9', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' OE1', ' OE2']
    residue['ASN'] = ['8', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' OD1', ' ND2']
    residue['GLN'] = ['9', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' OE1', ' NE2']
    residue['ARG'] = ['11', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' NE ', ' CZ ', ' NH1', ' NH2']
    residue['LYS'] = ['9', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' CE ', ' NZ ']
    residue['SER'] = ['6', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' OG ']
    residue['THR'] = ['7', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' OG1', ' CG2']
    residue['CYS'] = ['6', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' SG ']
    residue['MET'] = ['8', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' SD ', ' CE ']
    residue['PHE'] = ['11', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' CE1', ' CE2', ' CZ ']
    residue['TYR'] = ['12', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' CE1', ' CE2', ' CZ ', ' OH ']
    residue['HIS'] = ['10', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' ND1', ' CD2', ' CE1', ' NE2']
    residue['TRP'] = ['14', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' NE1', ' CE2', ' CE3', ' CZ2', ' CZ3', ' CH2']
    residue['PRO'] = ['7', ' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ']
    return residue[res]


def find_missing_atoms(atoms):
    missing_atom = 'THERE ARE NO MISSING ATOMS'
    atoms_in_residue = []
    residue_id = ''
    chain_id = ''
    residue_name = ''
    for line in atoms:
        chain_id = line[21]
        residue_id = int(line[22:26])
        residue_name = line[17:20]
        break
    for line in atoms:
        if int(line[22:26]) != residue_id or line[21] != chain_id:
            full_atom_list = get_residue_contents(residue_name)
            if int(full_atom_list[0]) != len(atoms_in_residue):
                for i in range(1, len(full_atom_list)):
                    if full_atom_list[i] not in atoms_in_residue:
                        missing_atom = 'MISSING ATOM %s IN: %s %s %s' % (full_atom_list[i], chain_id, residue_name, residue_id)
                        break
            atoms_in_residue = []
            chain_id = line[21]
            residue_id = int(line[22:26])
            residue_name = line[17:20]
        if (line[12:16]) != ' OXT':
            atoms_in_residue.append(line[12:16])
        full_atom_list = get_residue_contents(residue_name)

    if int(full_atom_list[0]) != len(atoms_in_residue):
        for i in range(1, len(full_atom_list)):
            if full_atom_list[i] not in atoms_in_residue:
                missing_atom = 'MISSING ATOM %s IN: %s %s %s' % (full_atom_list[i], chain_id, residue_name, residue_id)
                break
    return missing_atom


def find_missing_residues(atoms):
    missing_residue = 'THERE ARE NO MISSING RESIDUES'
    coord_N = {}
    coord_C = {}
    for line in atoms:
        chain_id = line[21]
        residue_id = line[22:26]
        if line[12:16] == ' C  ':
            coord_C['%s%s' % (chain_id, residue_id)] = line
        elif line[12:16] == ' N  ':
            coord_N['%s%s' % (chain_id, residue_id)] = line
    residue_id = ''
    chain_id = ''
    for line in atoms:
        chain_id = line[21]
        residue_id = line[22:26]
        break
    for line in atoms:
        if line[21] != chain_id:
            chain_id = line[21]
            residue_id = line[22:26]
        if int(line[22:26]) != int(residue_id) and int(line[22:26]) != (int(residue_id)+1):
            distance_C_N = get_distance(coord_C['%s%s' % (chain_id, residue_id)], coord_N['%s%s' % (line[21], line[22:26])])
            print('Suspicious %s%s: C-N %f' % (line[21], line[22:26], distance_C_N))
            if distance_C_N > 1.40:
                missing_residue = 'MISSING RESIDUE BEFORE: %s' % line[17:26]
                break
        residue_id = line[22:26]
    return missing_residue


if __name__ == '__main__':
    main_directory = 'C:\\development\\sources\\'
    atoms = read_pdb_file('%s\\%s' % (main_directory, 'missing1.pdb'))
    #atoms = read_pdb_file('%s\\%s' % (main_directory, 'missing2.pdb'))
    #atoms = read_pdb_file('%s\\%s' % (main_directory, 'missing3.pdb'))
    #atoms = read_pdb_file('%s\\%s' % (main_directory, 'missing4.pdb'))
    #atoms = read_pdb_file('%s\\%s' % (main_directory, 'missing5.pdb'))
    #atoms = read_pdb_file('%s\\%s' % (main_directory, 'missing6.pdb'))
    print(find_missing_atoms(atoms))
    print(find_missing_residues(atoms))
