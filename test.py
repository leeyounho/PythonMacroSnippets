import pandas as pd
from bs4 import BeautifulSoup
import xlwings as xw

# Step 1: Parse the HTML file with BeautifulSoup
with open(r'C:\Users\younho\Desktop\test.htm', 'r', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# Step 2: Extract the data you want from the HTML file
table = soup.find('table')

rows = []
for tr in table.tbody.find_all('tr'):
    row = []
    for td in tr.find_all(['td', 'th']):
        cell = td.get_text(strip=True)
        row.append(cell)
    rows.append(row)

# Step 3: Convert the data to a Pandas dataframe
df = pd.DataFrame(rows)

# Step 4: Create a new Excel workbook and sheet, and add the data to it
wb = xw.Book()
sheet = wb.sheets.add()

sheet.range('A1').value = df.values

# Step 5: Save the Excel file
wb.save('output.xlsx')