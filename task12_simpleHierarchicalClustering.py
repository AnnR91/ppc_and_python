from task3_readPDB import read_pdb_file
from task4_RMSD import get_rmsd

if __name__ == '__main__':
    threshold = 3.0
    input_directory = 'C:\\development\\sources\\'
    output_directory = 'C:\\development\\workdir\\'
    energies_file = open('%s\\1KXP_energies_reduced.txt' % input_directory).readlines()
    energies = []
    already_clustered = []
    for line in energies_file:
        spline = line.split()
        my_tuple = (spline[0], float(spline[1]))
        energies.append(my_tuple)
    energies.sort(key=lambda x: x[1])

    output = open('%s\\clusters_reduced.txt' % output_directory, 'w')

    for i in range(0, len(energies)):
        structure1 = energies[i][0]
        if structure1 in already_clustered:
            continue
        new_cluster = [structure1]
        already_clustered.append(structure1)
        atoms1 = read_pdb_file('%s\\afterSplit\\%s' % (output_directory, '%s_lig.pdb' % structure1[0:-4]))
        s1_tuple = []
        for atom_line_1 in atoms1:
            if atom_line_1[0:4] == 'ATOM':
                coord_tuple = (float(atom_line_1[30:38].strip()), float(atom_line_1[38:46].strip()), float(atom_line_1[46:54].strip()))
                s1_tuple.append(coord_tuple)
        counter = 0
        for j in range(i+1, len(energies)):
            structure2 = energies[j][0]
            if structure2 in already_clustered:
                continue
            counter += 1
            atoms2 = read_pdb_file('%s\\afterSplit\\%s' % (output_directory, '%s_lig.pdb' % structure2[0:-4]))
            s2_tuple = []
            for atom_line_2 in atoms2:
                if atom_line_2[0:4] == 'ATOM':
                    coord_tuple = (float(atom_line_2[30:38].strip()), float(atom_line_2[38:46].strip()), float(atom_line_2[46:54].strip()))
                    s2_tuple.append(coord_tuple)

            rmsd = get_rmsd(s1_tuple, s2_tuple)
            if rmsd < threshold:
                new_cluster.append(structure2)
                already_clustered.append(structure2)
        print('CHECKED %i ... PROGRESS %.2f %%' % (counter, (100.0 * float(len(already_clustered)) / float(len(energies)))))
        output.write('%s\n' % new_cluster)
        print(new_cluster)
    output.close()
