def get_classification(irmsd, lrmsd, fnat):
    if fnat < 0.1 or lrmsd > 10.0 and irmsd > 4.0:
        return "Incorrect"
    elif fnat >= 0.3 and lrmsd > 5.0 and irmsd > 2.0:
        return "Acceptable"
    elif (fnat >= 0.1 and fnat < 0.3) and (lrmsd <= 10.0 or irmsd <= 4.0):
        return "Acceptable"
    elif fnat >= 0.5 and lrmsd > 1.0 and irmsd > 1.0:
        return "Medium"
    elif (fnat >= 0.3 and fnat < 0.5) and (lrmsd <= 5.0 or irmsd <= 2.0):
        return "Medium"
    elif fnat >= 0.5 and lrmsd <= 1.0 and irmsd <= 1.0:
        return "High"
    else:
        return "NO_CATEGORY"

number_to_structure = {}
map_file = open("C:\\development\\sources\\task0_mapfile.txt").readlines()
for line in map_file:
    spline = line.strip().split()
    structure = spline[0].replace('1kxp_','').replace('la','a').replace('lb','b').replace('lc','c').replace('ld','d')
    number = spline[1]
    number_to_structure[number] = structure

properties_file = open("C:\\development\\sources\\task0_properties.txt").readlines()
output = open("C:\\development\\workdir\\task0_output.txt", 'w')
for line in properties_file:
    spline = line.split()
    number = spline[1]
    irmsd = float(spline[3])
    lrmsd = float(spline[4])
    fnat = float(spline[5])
    classification = get_classification(irmsd, lrmsd, fnat)
    output.write('%s\t%s\n'%(number_to_structure[number], classification))
output.close()
