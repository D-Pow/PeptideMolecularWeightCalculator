def calculate(string):
    total = 0.0
    for letter in string:
        if letter == 'F' or letter == 'f':
            total += 147.1761
        elif letter == 'I' or letter == 'i':
            total += 113.1588
        elif letter == 'L' or letter == 'l':
            total += 113.1588
        elif letter == 'K' or letter == 'k':
            total += 128.1734
        elif letter == 'M' or letter == 'm':
            total += 131.1976
        elif letter == 'T' or letter == 't':
            total += 101.1049
        elif letter == 'W' or letter == 'w':
            total += 186.2114
        elif letter == 'V' or letter == 'v':
            total += 99.1321
        elif letter == 'R' or letter == 'r':
            total += 156.1869
        elif letter == 'H' or letter == 'h':
            total += 137.1404
        elif letter == 'A' or letter == 'a':
            total += 71.0787
        elif letter == 'N' or letter == 'n':
            total += 114.1036
        elif letter == 'D' or letter == 'd':
            total += 115.0884
        elif letter == 'C' or letter == 'c':
            total += 103.1442
        elif letter == 'E' or letter == 'e':
            total += 129.1151
        elif letter == 'Q' or letter == 'q':
            total += 128.1303
        elif letter == 'G' or letter == 'g':
            total += 57.0521
        elif letter == 'P' or letter == 'p':
            total += 97.1162
        elif letter == 'S' or letter == 's':
            total += 87.0782
        elif letter == 'Y' or letter == 'y':
            total += 163.1746
        elif letter == 'X' or letter == 'x':
            total += 143.1411
        elif letter == 'Z' or letter == 'z':
            total += 124.1394
        elif letter == 'B' or letter == 'b':
            total += 243.1533
        #print 'Peptide is:', letter, 'Total is:', total
    return total

def main():
    peptide = raw_input('''Type the name of your peptide.
If it includes taurine, Yp, or the ester compound:
write "Z" for taurine, "B" for Yp, and "X" for ester.\n''')
    if peptide[0:3] == 'Nap' or peptide[0:3] == 'nap':
        #print 'Pre is:', peptide[0:3], 'Post is:', peptide[3:]
        total = calculate(peptide[3:])
        total += 169.2021
    elif peptide[0:4] == 'Fmoc' or peptide[0:4] == 'fmoc':
        #print 'Pre is:', peptide[0:4], 'Post is:', peptide[4:]
        total = calculate(peptide[4:])
        total += 223.2499
    else:
        #print 'Protein is:', peptide
        total = calculate(peptide)
        total += 1.0079
    #print 'Last is:', peptide[-1]
    total += 17.0069
    #print 'OH was added'
    if peptide[-1] == 'Z' or peptide[-1] == 'z':
        #print 'I will remove OH'
        #print 'Total before:', total
        total = total - 17.0069
        #print 'Total after:', total
    print 'Molecular weight is:', total, 'g/mol\n'
    another = raw_input('Want to find another compound? Y/N\n')
    if another == 'Y' or another == 'y':
        main()
    else:
        return

if __name__ == "__main__":
    main()
