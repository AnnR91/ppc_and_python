from task3_readPDB import read_pdb_file


def get_sequence(atoms):
    """
    :param atoms: ATOM records
    :type s: list
    :return: one letter code sequence
    """
    res3lett = ['GLY', 'ALA', 'LEU', 'ILE', 'VAL', 'ASP', 'GLU', 'ASN', 'GLN', 'ARG', 'LYS', 'SER', 'THR', 'CYS', 'MET',
                'PHE', 'TYR', 'HIS', 'TRP', 'PRO']
    res1lett = ['G', 'A', 'L', 'I', 'V', 'D', 'E', 'N', 'Q', 'R', 'K', 'S', 'T', 'C', 'M', 'F', 'Y', 'H', 'W', 'P']
    sequence = ''
    current_residue = -1
    current_chain = -1
    sequences = []
    length_counter = 0
    for line in atoms:
        if line[0:4] == 'ATOM':
            if line[21] != current_chain:
                current_chain = line[21]
                current_residue = -1
                if len(sequence) > 0:
                    sequences.append(sequence)
                    sequence = ''
                    length_counter = 0
            if line[22:26] != current_residue:
                residue_name = line[17:20]
                position = [i for i, j in enumerate(res3lett) if j == residue_name]
                if len(position) == 1:
                    sequence += res1lett[position[0]]
                    length_counter += 1
                    if length_counter % 80 == 0:
                        sequence += '\n'
                else:
                    print('ERROR: cannot find residue %s' % residue_name)
                    return ''
                current_residue = line[22:26]
            if current_residue == -1:
                current_residue = line[22:26]
            if current_chain == -1:
                current_chain = line[21]
    sequences.append(sequence)
    output_sequence = ''
    for i in range(0, len(sequences)):
        output_sequence += '%s\n\n' % sequences[i]
    return output_sequence

if __name__ == '__main__':
    main_directory = 'C:\\development\\sources'
    atoms = read_pdb_file('%s\\1KXP_dockedPoses\\%s' % (main_directory, '0a.pdb'))
    print(get_sequence(atoms))

