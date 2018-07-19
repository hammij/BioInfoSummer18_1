import csv

list_of_inputs = []
f = open('UCSC_Genes_hg19.txt', 'r')
with open('UCSC_Genes_hg19.txt', 'r') as f:
    next(f) # skip heading
    reader = csv.reader(f, delimiter = '\t')
    for name, chrom, strand, txStart, txEnd, cdsStart, cdsEnd, exonCount, exonStarts,exonEnds, proteinID, alignID in reader:
        temp = []
        temp = [name, chrom, strand, txStart, txEnd, cdsStart, cdsEnd, exonCount, exonStarts, exonEnds, proteinID, alignID]
        list_of_inputs.append(temp)


def n_overlap(f_in, f_out):
    pe_list = []
    f = open(f_in, 'r') #file readin
    with open(f_in, 'r') as f:
        reader = csv.reader(f, delimiter = '\t')
        for enhance, chrom, start, end, gene in reader:
             for i in range(len(list_of_inputs)): #will check each overlap readin against every entry in masterfile
                place_holder = list_of_inputs[i]
                if(chrom == place_holder[1] and start < place_holder[3] and place_holder[3] < end): #if chromosome overlap matches chrmosome from masterfile and overlaps the master start
                    temp_list = [enhance + '_' + chrom + '_' + start + '_' + end, gene, 'promoter']
                    pe_list.append(temp_list) #add to promoter list
                elif(chrom == place_holder[1] and start > place_holder[3] or end < place_holder[3]): #if chromosome overlap matches chromosome from masterfile but doesnot overlap
                    temp_list = [enhance + '_' + chrom + '_' + start + '_' + end, gene, 'enhancer']
                    pe_list.append(temp_list)
                else:   #chromosome does not match chromosome from masterfile
                    temp_list = [enhance + '_' + chrom + '_' + start + '_' + end, gene, 'NA']
                        #nothing for now unless also needs to be enhancer region
    #pe_dict = {}
    #for n in range(len(pe_list)): #convert list to dictionary
    #    temp_var = pe_list[n]
    #    pe_dict[temp_var[0]] = temp_var[1]+ ','+temp_var[2]

    #w = csv.writer(open(f_out, 'wb'))
    #for key, value in pe_dict.items():
    #    w.writerow(key + '\t' + value)
    return(len(pe_list))
