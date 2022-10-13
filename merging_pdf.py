#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 02:28:29 2022

@author: dorianturk
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PageObject
from PyPDF2 import PdfMerger


pixel = 0.035285714285714 #cm

#range je 4 ili 8 ili 16 da ne radi uzalud sve odf-ove

pdf_svi_lista = []

for j in range(57):
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
merged_page = PageObject.createBlankPage(None, width, height)

split_lists = [pages[x:x+8] for x in range(0, len(pages), 8)]

for i in range(len(split_lists)):
    globals()[f"merged_page{str(i)}"] = PageObject.createBlankPage(None, width, height)
    print(i)
    j = i
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


