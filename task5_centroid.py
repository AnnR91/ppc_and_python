from task3_readPDB import read_pdb_file
#import sys
import argparse


def get_centroid(s):
    """
    :param s: x,y,z coordinates of structure
    :type s: tuple
    :return: centroid as tuple (x,y,z)
    """
    x = 0.0
    y = 0.0
    z = 0.0
    for i in range(0,len(s)):
        x += s[i][0]
        y += s[i][1]
        z += s[i][2]
    x /= len(s)
    y /= len(s)
    z /= len(s)
    return round(x, 3), round(y, 3), round(z, 3)

if __name__ == '__main__':
    main_directory = 'C:\\development\\workdir\\'

    #first version without argparse
    #file_name = sys.argv[1]

    parser = argparse.ArgumentParser(description='Calculate centroid.')
    parser.add_argument('filename', help='a name of PDB file')
    args = parser.parse_args()

    #atoms = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, '0a_lig.pdb'))
    atoms = read_pdb_file('%s\\afterSplit\\%s' % (main_directory, args.filename))
    s_tuple = []
    for atom_line in atoms:
        if atom_line[0:4] == 'ATOM':
            coord_tuple = (float(atom_line[30:38].strip()),float(atom_line[38:46].strip()),float(atom_line[46:54].strip()))
            s_tuple.append(coord_tuple)

    #cx, cy, cz = get_centroid(s_tuple)
    #print(cx, cy, cz)
    print(get_centroid(s_tuple))
