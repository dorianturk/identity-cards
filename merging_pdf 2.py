#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 02:28:29 2022

@author: dorianturk
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PageObject
from PyPDF2 import PdfMerger
import numpy as np

pixel = 0.035285714285714 #cm

#range je 4 ili 8 ili 16 da ne radi uzalud sve odf-ove

pdf_svi_lista = []

for j in range(4):
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


#Open the files that have to be merged
pdf1File = open('merged-pdf.pdf', 'rb')

#Read the files that you have opened
pdf1Reader = PdfFileReader(pdf1File)

pages = []
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pages.append(pageObj)

#width = pages[0].mediaBox.getWidth() * 2
#height = pages[0].mediaBox.getHeight() + 100

width = 21 / pixel
height = (29.7 / pixel)*7

x=0
y=0

merged_page = PageObject.createBlankPage(None, width, height)

k=0
for page in pages:
    #print(f"list br {a}")
    merged_page.mergeScaledTranslatedPage(page, scale=1, tx=x, ty=y)
    for x in range(10,int(190/10/pixel),int(95/10/pixel)):
        for y in range(18,int(278/10/pixel),int(65/10/pixel)):
             
            print(f"dodao iskaznicu {k} na lokaciju {x,y} u pdf-u")
        k += 1

 
writer = PdfFileWriter()
writer.addPage(merged_page)
with open("spojeni_jedna_str.pdf", 'wb') as f:
    writer.write(f)

print("Spojeno je sve u jedan PDF!")


"""novo
for page in pages:
    merged_page.mergeScaledTranslatedPage(page, scale=1, tx=x, ty=y)  
    if x < float(page.mediaBox.getWidth()):
        x = float(x) + float(page.mediaBox.getWidth()) 
    elif y < 30 * float(page.mediaBox.getHeight()):
        x = 0
        y = float(y) + float(page.mediaBox.getHeight())        
"""

"""
for i in range(int(len(pages)/8+1)):
    print(i)
    globals()[f"merged_page{str(i)}"] = PageObject.createBlankPage(None, width, height)
    globals()[f"x{str(i)}"] = 0
    globals()[f"y{str(i)}"] = 0
    
    for page in pages:
        vars()[f"merged_page{str(i)}"].mergeScaledTranslatedPage(page, scale=1, tx=vars()[f"x{str(i)}"], ty=vars()[f"y{str(i)}"])
        if vars()[f"x{str(i)}"] < float(page.mediaBox.getWidth()):
            vars()[f"x{str(i)}"] = float(vars()[f"x{str(i)}"]) + float(page.mediaBox.getWidth()) 
        elif vars()[f"y{str(i)}"] < 3 * float(page.mediaBox.getHeight()):
            vars()[f"x{str(i)}"] = 0
            vars()[f"y{str(i)}"] = float(vars()[f"y{str(i)}"]) + float(page.mediaBox.getHeight())        
            
    writer = PdfFileWriter()
    writer.addPage(vars()[f"merged_page{str(i)}"])
    with open(f'spojeni_jedna_str{i}.pdf', 'wb') as f:
        writer.write(f)

    print("Spojeno je sve u jedan PDF!")

"""

"""

for page in pages:
    merged_page1.mergeScaledTranslatedPage(page, scale=1, tx=x, ty=y)  
    if x < float(page.mediaBox.getWidth()):
        x = float(x) + float(page.mediaBox.getWidth()) 
    elif y < 3 * float(page.mediaBox.getHeight()):
        x = 0
        y = float(y) + float(page.mediaBox.getHeight())        
    else:
        x = 100000
        y = 100000
        merged_page2.mergeScaledTranslatedPage(page, scale=1, tx=x1, ty=y1)
        
        if x1 < float(page.mediaBox.getWidth()):
            x1 = float(x1) + float(page.mediaBox.getWidth()) 
        elif y1 < 3 * float(page.mediaBox.getHeight()):
            x1 = 0
            y1 = float(y1) + float(page.mediaBox.getHeight())
        else:
            x1 = 100000
            y1 = 100000
            merged_page3.mergeScaledTranslatedPage(page, scale=1, tx=x2, ty=y2)
            
            if x2 < float(page.mediaBox.getWidth()):
                x2 = float(x2) + float(page.mediaBox.getWidth()) 
            elif y2 < 3 * float(page.mediaBox.getHeight()):
                x2 = 0
                y2 = float(y2) + float(page.mediaBox.getHeight())
            else:
                x2 = 100000
                y2 = 100000
                merged_page4.mergeScaledTranslatedPage(page, scale=1, tx=x3, ty=y3)
                
                if x3 < float(page.mediaBox.getWidth()):
                    x3 = float(x3) + float(page.mediaBox.getWidth()) 
                elif y3 < 3 * float(page.mediaBox.getHeight()):
                    x3 = 0
                    y3 = float(y3) + float(page.mediaBox.getHeight())
                else:
                    x3 = 100000
                    y3 = 100000
                    merged_page5.mergeScaledTranslatedPage(page, scale=1, tx=x4, ty=y4)
                    
                    if x4 < float(page.mediaBox.getWidth()):
                        x4 = float(x4) + float(page.mediaBox.getWidth()) 
                    elif y4 < 3 * float(page.mediaBox.getHeight()):
                        x4 = 0
                        y4 = float(y4) + float(page.mediaBox.getHeight())
                    else:
                        x4 = 100000
                        y4 = 100000
                        merged_page6.mergeScaledTranslatedPage(page, scale=1, tx=x5, ty=y5)
                        
                        if x5 < float(page.mediaBox.getWidth()):
                            x5 = float(x5) + float(page.mediaBox.getWidth()) 
                        elif y5 < 3 * float(page.mediaBox.getHeight()):
                            x5 = 0
                            y5 = float(y5) + float(page.mediaBox.getHeight())
                        else:
                            x5 = 100000
                            y5 = 100000
                            merged_page7.mergeScaledTranslatedPage(page, scale=1, tx=x6, ty=y6)
                            
                            if x6 < float(page.mediaBox.getWidth()):
                                x6 = float(x6) + float(page.mediaBox.getWidth()) 
                            elif y6 < 3 * float(page.mediaBox.getHeight()):
                                x6 = 0
                                y6 = float(y6) + float(page.mediaBox.getHeight())
                            else:
                                x6 = 100000
                                y6 = 100000
                                merged_page8.mergeScaledTranslatedPage(page, scale=1, tx=x7, ty=y7)
                                
                                if x7 < float(page.mediaBox.getWidth()):
                                    x7 = float(x7) + float(page.mediaBox.getWidth()) 
                                elif y7 < 3 * float(page.mediaBox.getHeight()):
                                    x7 = 0
                                    y7 = float(y7) + float(page.mediaBox.getHeight())
                                else:
                                    x7 = 100000
                                    y7 = 100000
                                    merged_page9.mergeScaledTranslatedPage(page, scale=1, tx=x8, ty=y8)
                                    
                                    if x8 < float(page.mediaBox.getWidth()):
                                        x8 = float(x8) + float(page.mediaBox.getWidth()) 
                                    elif y8 < 3 * float(page.mediaBox.getHeight()):
                                        x8 = 0
                                        y8 = float(y8) + float(page.mediaBox.getHeight())
                                    else:
                                        x8 = 100000
                                        y8 = 100000
                                    merged_page10.mergeScaledTranslatedPage(page, scale=1, tx=x9, ty=y9)
                                    
                                    if x9 < float(page.mediaBox.getWidth()):
                                        x9 = float(x9) + float(page.mediaBox.getWidth()) 
                                    elif y9 < 3 * float(page.mediaBox.getHeight()):
                                        x9 = 0
                                        y9 = float(y9) + float(page.mediaBox.getHeight())
                                    else:
                                        x9 = 100000
                                        y9 = 100000
             
                                 
          
  

writer.addPage(merged_page1)
writer.addPage(merged_page2)
writer.addPage(merged_page3)
writer.addPage(merged_page4)
writer.addPage(merged_page5)
writer.addPage(merged_page6)
writer.addPage(merged_page7)
writer.addPage(merged_page8)
writer.addPage(merged_page9)
#writer.addPage(merged_page10)
"""
"""
merged_page = PageObject.createBlankPage(None, width, height)

x = 0
y = 0

data = np.array(pages)
shape = (2, 2)

data = data.reshape( shape )

print(data)

for page in data:
    merged_page.mergeScaledTranslatedPage(page, scale=1, tx=x, ty=y)
    

"""
"""
writer = PdfFileWriter()
"""


