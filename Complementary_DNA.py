def DNA_strand(dna):
    # code here
    lst = list(dna)
    new = ""
    for x in lst:
        if x == 'A':
            new += 'T'
        if x == 'T':
            new += 'A'
        if x == 'C':
            new += 'G'
        if x == 'G':
            new += 'C'
    return new

# takes extremely long pairs is a much shorter solution
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])


    

print(DNA_strand("CCAATT"))