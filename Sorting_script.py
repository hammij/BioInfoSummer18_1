#Sorts entries based on activity, then creates tsv for each type

import csv

Blood_cancer = {}
Blood_healthy = {}
Breast_cancer = {}
Breast_healthy = {}
Liver_cancer = {}
Liver_healthy = {}
Pancreas_cancer = {}
Pancreas_Healthy = {}

f = open('Allgenes_activity.tsv', 'r')
with open('Allgenes_activity.tsv') as f:
        next(f) #skips headings
        reader = csv.reader(f, delimiter = '\t')
        for name, gene, bloodc_act, bloodh_act, breastc_act, breasth_act, liverc_act, liverh_act, pancreasc_act, pancreash_act in reader:
            if(bloodc_act == 'on'):
                Blood_cancer[name] = gene
            if(bloodh_act == 'on'):
                Blood_healthy[name] = gene
            if(breastc_act == 'on'):
                Breast_cancer[name] = gene
            if(breastc_act == 'on'):
                Breast_healthy[name] = gene
            if(liverc_act == 'on'):
                Liver_cancer[name] = gene
            if(liverh_act == 'on'):
                Liver_healthy[name] = gene
            if(pancreasc_act == 'on'):
                Pancreas_cancer[name] = gene
            if(pancreash_act == 'on'):
                Pancreas_Healthy[name] = gene

w = csv.writer(open("Blood_Cancer.tsv", "w"))
for key, val in Blood_cancer.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Blood_Healthy.tsv", "w"))
for key, val in Blood_healthy.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Breast_Cancer.tsv", "w"))
for key, val in Blood_cancer.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Breast_Healthy.tsv", "w"))
for key, val in Breast_healthy.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Liver_Cancer.tsv", "w"))
for key, val in Liver_cancer.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Liver_Healthy.tsv", "w"))
for key, val in Liver_healthy.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Pancreas_Cancer.tsv", "w"))
for key, val in Pancreas_cancer.items():
    w.writerow([key + '\t' + val])

w = csv.writer(open("Pancreas_Healthy.tsv", "w"))
for key, val in Pancreas_Healthy.items():
    w.writerow([key + '\t' + val])
