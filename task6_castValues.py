from math import fabs


def cast_values(energies_file):
    energies_dict = {}
    energies_tuple = []
    input_file = open(energies_file).readlines()
    highest = -99999.0
    for line in input_file:
        spline = line.split()
        my_tuple = (spline[0], float(spline[1]))
        if my_tuple[1] > highest:
            highest = my_tuple[1]
        energies_tuple.append(my_tuple)
    energies_tuple.sort(key=lambda x: x[1])
    # print(energies_tuple[0][1], highest)

    smallest_abs = fabs(energies_tuple[0][1])

    # move everything to positive numbers
    for i in range(0, len(energies_tuple)):
        energies_dict[energies_tuple[i][0]] = energies_tuple[i][1] + smallest_abs
    highest += smallest_abs

    # 10 * (value_i / highest), normalization to 1 and multiplication by 10
    for i in range(0, len(energies_tuple)):
        energies_dict[energies_tuple[i][0]] = round(10.0 * (energies_dict[energies_tuple[i][0]]/highest), 2)

    return energies_dict

if __name__ == '__main__':
    main_directory = 'C:\\development\\sources'
    processed = cast_values('%s\\%s' % (main_directory, '1KXP_energies.txt'))
    print(processed['9d.pdb'])
