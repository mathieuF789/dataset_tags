import os
import csv
import fastwer


# Fonction permettant de lire un fichier csv
def readCSV(filename):
	out = []
	with open(filename,encoding='utf-8') as csvfile:
		data = csv.reader(csvfile, delimiter='¤',quotechar=None)
		for row in data:
			out.append(row)
		return out


cer_total = 0
wer_total = 0

val_gt = readCSV('./tags_2/gt/gt.txt')
val_ocr = readCSV('./tags_2/ocr_output/paddle_b.txt')

if(len(val_gt) == len(val_ocr)):
	for i in range(1,len(val_gt)):
		cer = fastwer.score_sent(val_ocr[i][1], val_gt[i][1], char_level=True)
		wer = fastwer.score_sent(val_ocr[i][1], val_gt[i][1])

		if(wer > 0):
			wer = 100.0

		cer_total += cer
		wer_total += wer

	len_total = len(val_gt)-1

	cer_total /= len_total
	wer_total /= len_total

	fileOut = open('./tags_2/metrix_ocr/paddle_b_eval.txt','w')
	fileOut.write('CER : ' + str(cer_total) + '\n')
	fileOut.write('WER : ' + str(wer_total) + '\n')
	fileOut.close()