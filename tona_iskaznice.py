#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 00:49:41 2022

@author: dorianturk
"""
import pandas as pd
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PageObject
from PyPDF2 import PdfMerger

logo = input("Odabrani logo mobi3/mobi4/mobi5: ")
logoodabir = "NaN1"
korekcija_naslova = "NaN2"

df = pd.read_excel("Sažetci - popis.xlsx", header=0, skipfooter=1, index_col=None, usecols='A:B')
df_ime = df['Ime']
df_prezime = df['Prezime']

imena_list = df_ime.values.tolist()
prezimena_list = df_prezime.values.tolist()

print(df)
print(imena_list)
print(prezimena_list)  

if logo == 'mobi5':
    logoodabir = "logo_mobi5.jpg"
    korekcija_naslova = "-0.7 cm"
elif logo == 'mobi4':
    logoodabir = "logo_mobi4.jpg"
    korekcija_naslova = "0.3 cm"
elif logo == 'mobi3':
    logoodabir = "logo_mobi3.jpg"
    korekcija_naslova = "-0.35 cm"
else:
    print("Netocan odabir!")
    
for j in range(len(imena_list)):
    #print(f"{i} {imena_list[i]} {prezimena_list[i]}")
    IMEiPREZIME = f"{imena_list[j]} {prezimena_list[j]}"
    print(IMEiPREZIME)
    
    texdoc = []
    
    with open('Tona_iskaznice.tex', encoding = 'UTF-8') as fin:
        for line in fin:
            texdoc.append(line.replace('korekcija_naslova', korekcija_naslova).replace('IMEiPREZIME', IMEiPREZIME).replace('logoodabir', logoodabir))
            
    with open(f'edited/iskaznica{j}.tex', 'w', encoding = 'UTF-8') as fout:
        for i in range(len(texdoc)):
            fout.write(texdoc[i])
    
os.chdir("edited/")

for j in range(len(imena_list)):
    os.system(f"pdflatex iskaznica{j}.tex")
    
#izrada zajednickog pdf-a
pixel = 0.035285714285714 #cm

pdf_svi_lista = []

for j in range(len(imena_list)):
    pdf_svi_lista.append(f"iskaznica{j}.pdf")
print(pdf_svi_lista)
#-------------------
merger = PdfMerger()

for pdf in pdf_svi_lista:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
print("Napravljen je zajednicki pdf sa iskaznicom po listu!")
#-------------------
pdf1File = open('merged-pdf.pdf', 'rb')

pdf1Reader = PdfFileReader(pdf1File)

pages = []
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pages.append(pageObj)

width = 21 / pixel
height = (29.7 / pixel)

x=30
y=50
x1=x
y1=y

split_lists = [pages[x:x+8] for x in range(0, len(pages), 8)]

for i in range(len(split_lists)):
    globals()[f"merged_page{str(i)}"] = PageObject.createBlankPage(None, width, height)
    print(i)
    for page in split_lists[i]:
        vars()[f"merged_page{str(i)}"].mergeScaledTranslatedPage(page, scale=1, tx=x, ty=y)
        print(f"spremam iskaznicu {pages.index(page)} na lokaciju {x,y} ")
        if y < 3 * int(65/10/pixel):
            y = y + int(65/10/pixel)
        else:
            y = y1
            x = x + int(95/10/pixel)
    j = i + 1
    if j > i:
        x = x1
        y = y1
        print(j)
  
writer = PdfFileWriter()
for i in range(len(split_lists)):
    writer.addPage(vars()[f"merged_page{str(i)}"])
    
with open("a4_print.pdf", 'wb') as f:
    writer.write(f)

print("Spojeno je sve u jedan PDF!")