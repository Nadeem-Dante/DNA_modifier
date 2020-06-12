def translate(dna):
    #Write a function called translate that, when given a DNA sequence of arbitrary length, 
    #identifies and returns the amino acid sequence of the DNA using the amino acid SLC code.
    #For example: DNA Input: ATTCTCATA Output: ILI  
    table = { 
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
	'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
	'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
	} 
    aminosequence = "" 
    #runs through the DNA sequence taking strings of 3 in length
    for x in range(0, len(dna), 3): 
        #finds the 3 length codon
        codon = dna[x:x + 3] 
        #tests if the codon is in the table
        if codon in table:
            #adds the amino
            aminosequence += table[codon]
        else:
            #adds an X because it doesn't contain an amino
            aminosequence += "X"
    print(aminosequence)

translate('AACAAACAATTTCCGTATAATCTTAATACATGGTGTAATCGTACCGGGACGGTTTCGCGAGCATAGTGTACTTATATACAGTACTACGGACATGATAGTGGGTGTAAGAATACCCCCGGTGTACCTTGACACGGACTTGCAGGCATGCCTACCGTCG')
