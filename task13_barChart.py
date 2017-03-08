from task3_readPDB import read_pdb_file
from task8_printSequence import get_sequence
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    main_directory = 'C:\\development\\sources'
    atoms = read_pdb_file('%s\\1KXP_dockedPoses\\%s' % (main_directory, '0a.pdb'))
    sequence = get_sequence(atoms)

    seqsplit = sequence.split('\n')
    chains = []
    position = 0
    sequence = ''
    while position < len(seqsplit):
        if seqsplit[position] != '':
            sequence += seqsplit[position]
        else:
            if len(sequence) > 0:
                chains.append(sequence)
            sequence = ''
        position += 1

    res1lett = ['G', 'A', 'L', 'I', 'V', 'D', 'E', 'N', 'Q', 'R', 'K', 'S', 'T', 'C', 'M', 'F', 'Y', 'H', 'W', 'P']
    res_dictionary = {'CHAIN A': {}, 'CHAIN B': {}}
    for res in res1lett:
        res_dictionary['CHAIN A'][res] = 0
        res_dictionary['CHAIN B'][res] = 0
    for letter in chains[0]:
        res_dictionary['CHAIN A'][letter] += 1
    for letter in chains[1]:
        res_dictionary['CHAIN B'][letter] += 1

    print(res_dictionary)
    #http: // matplotlib.org / examples / api / barchart_demo.html
    ind = np.arange(len(res1lett))
    #print(ind)
    width = 0.35
    chainA_counts = []
    chainB_counts = []
    for i in res1lett:
        chainA_counts.append(res_dictionary['CHAIN A'][i])
        chainB_counts.append(res_dictionary['CHAIN B'][i])

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, chainA_counts, width, color='r')
    rects2 = ax.bar(ind + width , chainB_counts, width, color='y')
    ax.set_ylabel('Count')
    ax.set_title('Count by aminoacid and chain')
    ax.set_xticks(ind + width /2)
    ax.set_xticklabels(res1lett)
    ax.legend((rects1[0], rects2[0]), ('Chain A', 'Chain B'))

    plt.show()
