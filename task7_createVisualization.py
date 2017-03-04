from task6_castValues import cast_values
from task5_centroid import get_centroid
from task3_readPDB import read_pdb_file

"""
COLUMNS        DATA  TYPE    FIELD        DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name   "ATOM  "
 7 - 11        Integer       serial       Atom  serial number.
13 - 16        Atom          name         Atom name.
17             Character     altLoc       Alternate location indicator.
18 - 20        Residue name  resName      Residue name.
22             Character     chainID      Chain identifier.
23 - 26        Integer       resSeq       Residue sequence number.
27             AChar         iCode        Code for insertion of residues.
31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
55 - 60        Real(6.2)     occupancy    Occupancy.
61 - 66        Real(6.2)     tempFactor   Temperature  factor.
77 - 78        LString(2)    element      Element symbol, right-justified.
79 - 80        LString(2)    charge       Charge  on the atom.
"""

input_directory = 'C:\\development\\sources\\'
output_directory = 'C:\\development\\workdir\\'
processed_energies = cast_values('%s\\%s' % (input_directory, '1KXP_energies.txt'))

input_file = open('%s\\1KXP_dockedPoses\\filelist.txt' % input_directory).readlines()
file_list = []
for line in input_file:
    file_list.append(line[:-1])

output_file = open('%s\\visualization_ligands.pdb' % output_directory, 'w')

counter = 0
for file_name in file_list:
    atoms = read_pdb_file('%s\\afterSplit\\%s_lig.pdb' % (output_directory, file_name[0:-4]))
    s_tuple = []
    for atom_line in atoms:
        if atom_line[0:4] == 'ATOM':
            coord_tuple = (float(atom_line[30:38].strip()), float(atom_line[38:46].strip()), float(atom_line[46:54].strip()))
            s_tuple.append(coord_tuple)
    cx, cy, cz = get_centroid(s_tuple)
    counter += 1
    output_file.write('HETATM%5s%5s VIS X%4i    %8.3f%8.3f%8.3f  1.00%6.2f\n' % (str(counter), file_name.replace('.pdb', ''), 0, cx, cy, cz, processed_energies[file_name]))
output_file.close()
