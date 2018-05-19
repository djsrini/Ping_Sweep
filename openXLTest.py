from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active
sheet['A1'] = "Ping Status"
sheet['b1'] = "DNS Name"

now = time.strftime("%x")
sheet['A3'] = now

book.save("sample.xlsx")