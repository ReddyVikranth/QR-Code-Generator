import cv2
import numpy as np
import pandas as pd
from BasePrinter import base_printer
from DataTypePrinter import data_type_printer
from TimingStrips import timing_strips
from MasahiroHara import masahiro_hara
from QuiteZone import quite_zone
from Isolation import isolation
from FormatStrips import format_strips
from CharactersLength import characters_length
from FinalCut import final_cut
print("Enter the size of the QR code you want: (min: 21)")
size = int(input())
while(size < 21):
    print("Invalid size! give input again")
    size = int(input())
size += 2

base_qr = np.full((size,size),255)

base_printer(base_qr,size)

print("What kind of data you want to encode in the QR Code?")
print("1.Binary\n2.Alphanumeric\n3.Numerical\n4.Japanese kanji")
encode_type = int(input())
while(encode_type < 1 or encode_type > 4):
    print("Invalid choice. Please choose again")
    print("1.Numeric\n2.Alphanumeric\n3.Binary\n4.Japanese kanji")
    encode_type = int(input())
print("What name do you want your QRcode to have? (just the name, without any extentions)")
qr_name = str(input())
qr_name = qr_name + '.png'
quite_zone(base_qr,size)
data_type_printer(base_qr,size,encode_type)
isolation(base_qr,size)
timing_strips(base_qr,size)
format_strips(base_qr,size)
masahiro_hara(base_qr,size)


print("Enter the message that you want to encode: ")
data = str(input())
characters_length(base_qr,len(data),size)
final_cut(base_qr,size)
base_qr[size-11,size-2] = 0
base_qr[size-11,size-3] = 0
cv2.imwrite(qr_name,base_qr)