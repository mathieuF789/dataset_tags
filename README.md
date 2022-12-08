# Tags dataset
## Introduction

This dataset is composed of Tags images. The tags are the identifiers of the engineering technical components which are language model free and incomprehensible if we have neither engineering knowledge nor informations about the project. These data come from real industrial projects from different sectors of activity such as: hydraulic, gas and pharmaceutical.

The goal of this dataset is to represent a real industrial use case, which has been imagined as follows: An industrial engineer digitizes the plans of a project and is particularly interested in tags.  Several days later, he retrieves new documents from the same project and also wants to extract the tags. This engineer needs a transcription as close as possible to the ground truth to correctly identify the technical component.

## OCR Results

The OCR systems used are the following : 

* EasyOCR with the version 1.5.0
* PaddleOCR with the version 2.6.0.1
* Tesseract with the version 5.2.0


Below are calculations of the OCR quality output using the Character Error Rate (CER) and Word Error Rate (WER) metrix.

| Tags_1       | CER | WER     |
| ------------ | ----- | ----- |
| EasyOCR      | 8.71  | 53.79 |
| PaddleOCR    | 1.98  | 15.68 |
| PaddleOCR_b  | 3.85  | 29.89 |
| Tesseract    | 2.63  | 18.60 |

| Tags_2       | CER   | WER   |
| ------------ | ----- | ----- |
| EasyOCR      | 10.33 | 75.0  |
| PaddleOCR    | 25.15 | 79.03 |
| PaddleOCR_b  | 1.66  | 19.35 |
| Tesseract    | 1.62  | 23.39 |

## Content

The data is decomposed into two parts :

* tags_1/ : represents the data related to the tags images of 30 plans, that is 1570 images;
* tags_2/ : represents the data related to the tags images of 7 plans, that is 125 images ;
* eval.py : represents the evaluation code using the CER/WER metrix. We considered each Tag as a single 'word' even if it contains spaces. 

In the two folders tags_1 and tags_2, 4 subfolders are as follows :

* gt/ : contains the .csv file with the ground truth in the form: Image name,Ground truth ;
* img/ : contains the image files representing the tags ;
* metrix_ocr/ : contains the .txt files representing the OCR results via the CER/WER metrix;
* ocr_output/ : contains the .csv files representing the OCR predictions for each system in the form: Image Name, Prediction, Confidence.

## How it was created

The tag images and ground truth were originally extracted on searchable PDFs. Thanks to the PDFMiner library, the coordinates and the transcription of each text could be extracted via the documents' metadata. After that, each tag sub-image are converted into an image format and associated with their transcription.

Thanks to the automatic creation of the dataset, it should not contain any (or very few) ground truth errors. Do not hesitate to contact us if you find any.


## How to cite this dataset


