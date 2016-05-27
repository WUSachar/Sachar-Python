import csv


words = [""]
genes = [""]

cancerGenes = open('GeneSymbol.txt')
csv_words = csv.reader(cancerGenes)
for row in csv_words:
	for item in row:
		info = item.split()
		for one in info:
			genes.append(one.lower())

paper = open('Paper_1.txt')
csv_paper = csv.reader(paper)
for row in csv_paper:
	for item in row:
		info = item.split()
		for one in info:
			if one.lower() in genes:
				words.append(one)

uniqueGenes = []
for word in words:
   if word not in uniqueGenes:
	   uniqueGenes.append(word)

uniqueGeneCount = []
for gene in uniqueGenes:
	uniqueGeneCount.append(words.count(gene))

longestUniqueGene = -999
for i in range(1,len(uniqueGenes)):
	if len(str(uniqueGenes[i])) > longestUniqueGene:
		longestUniqueGene = len(str(uniqueGenes[i]))

uniqueGeneCountAverage = 0
total = 0
for i in range(1,len(uniqueGeneCount)):
	total += uniqueGeneCount[i]
uniqueGeneCountAverage = total / len(uniqueGeneCount)


print "Genes that are referenced more than average are denoted by *"
for i in range(1,len(uniqueGeneCount)):
	if uniqueGenes[i].isupper() and uniqueGeneCount[i] > uniqueGeneCountAverage:
		print uniqueGenes[i] + '{dash:>{width}}'.format(dash = '-' , width = longestUniqueGene-len(str(uniqueGenes[i])) +2)  + " " +str(uniqueGeneCount[i]) + "*"
	elif uniqueGenes[i].isupper():
		print uniqueGenes[i] + '{dash:>{width}}'.format(dash = '-' , width = longestUniqueGene-len(str(uniqueGenes[i])) +2)  + " " + str(uniqueGeneCount[i])


paper.close()
cancerGenes.close()

