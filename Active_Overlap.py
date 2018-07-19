import csv

f = open('Blood_Healthy.tsv', 'r') #file read in
with open('Blood_Healthy.tsv', 'r') as f:
    reader = csv.reader(f, delimiter = '\t')
    prev = None
    curr = []
    comp = []
    final_dic = {}
    for name, chr_name, start, end, gene in reader:
        curr = [name, chr_name, start, end, gene]
        if(prev == None): #first pass
            comp = curr
            prev = curr
        else: #not first pass
            if(prev[4] != curr[4]): #not the same gene
                temp = [comp[0]+'_'+comp[1]+'_'+comp[2]+'_'+comp[3], comp[4]] #formats for dictionary input
                final_dic[temp[0]] = temp[1] #adds to dictionary
                comp = curr
                prev = curr
            elif(prev[4] == curr[4] and prev[3] < curr[2]): #same gene but not overlap
                temp = [comp[0]+'_'+comp[1]+'_'+comp[2]+'_'+comp[3], comp[4]] #formats for dictionary input
                final_dic[temp[0]] = temp[1] #adds to dictionary
                comp = curr
                prev = curr
            elif(prev[4] == curr[4] and prev[3] > curr[2]): #same gene and overlap
                comp[3] = curr[3]
                prev = curr
    temp = [comp[0]+'_'+comp[1]+'_'+comp[2]+'_'+comp[3], comp[4]] #formats for dictionary input
    final_dic[temp[0]] = temp[1] #adds last compiled line to dictionary

w = csv.writer(open("Blood_Healthy_Overlap.tsv", "w")) #name of out file
for key, val in final_dic.items():
    w.writerow([key + '\t' + val])
