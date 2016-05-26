import csv

tert = open('20160204_ASU_TERT_database.txt')
csv_tert = csv.reader(tert)
for row in csv_tert:
    for item in row:
        info = item.split()
        if str(info[0]) == "TERT" and str(info[1][0])== "c":
            gene = info[0]
            HGVSc = info[1]
            HGVScStr = str(HGVSc)
            HGVSp = info[2]
            HGVSpStr = str(HGVSp)
            variant = HGVScStr[len(HGVScStr)-1]
            reference = HGVScStr[len(HGVScStr)-3]
            database = "ASU_TERT"
            chromosome_name = "NA"
            start = "NA"
            stop = "NA"
            gene_name = gene
            #name.write(gene)
            if (variant == "A" or variant == "T" or variant == "C" or variant == "G"):
                FinalTert =  database + " " +chromosome_name +" "+start +" " +stop + " " + reference +" "+ variant + " "+ gene +" " +HGVScStr+ " " +HGVSpStr
                print FinalTert


tert.close()

brca1 = open('BRCA1_BIC_Download_12122014_clinically_important.txt')
csv_brca1 = csv.reader(brca1)
for row in csv_brca1:
    for item in row:



