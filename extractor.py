#### Scrpit by [Nitish Gadangi](https://nitishgadangi.github.io)
## https://github.com/NitishGadangi/Jntuh-MemoData-Extraxtor
## 09July2020
from bs4 import BeautifulSoup
import requests
import hashlib
import xlsxwriter 

def generate_xls(all_memos):
	name=input('enter name for xl sheet: ')
	workbook = xlsxwriter.Workbook(f'{name}.xlsx')
	worksheet = workbook.add_worksheet()
	row=0
	col=0
	for memo in all_memos:
		worksheet.write_row(row, col,  tuple(memo))
		row += 1
	workbook.close()
	print(f"{name}.xlsx saved in current working direcrory")


BASE_URL="http://results.jntuhceh.ac.in/verify/memo/"

start=int(input('Enter start memo number: '))
ending=int(input('Enter ending memo number: '))
all_memos=[]
all_memos.append(['Roll No','Name','SGPA','Credits','Result Status','Subjects Passed','Branch','Memo No'])
for memo in range(start,ending+1):
	new_memo=[]
	hashh=hashlib.sha256(str(memo).encode()).hexdigest()
	code1=requests.get(BASE_URL+str(hashh))
	soup1=BeautifulSoup(code1.text,"html.parser")
	rollno=str(soup1.find('div',{'data-title':'Hall Ticket'}).text).strip()
	name=str(soup1.find('div',{'data-title':'Full Name'}).text).strip()
	branch=str(soup1.find('div',{'data-title':'Branch'}).text).strip()
	credits=str(soup1.find('div',{'data-title':'Credits'}).text).strip()
	sgpa=str(soup1.find('div',{'data-title':'SGPA'}).text).strip()
	res_status=str(soup1.find('div',{'data-title':'Result Status'}).text).strip()
	passes_subs=str(soup1.find('div',{'data-title':'Passed Subjects'}).text).strip()
	memo_num=str(soup1.find('div',{'data-title':'Memo Serial'}).text).strip()
	new_memo.append(rollno)
	new_memo.append(name)
	new_memo.append(sgpa)
	new_memo.append(credits)
	new_memo.append(res_status)
	new_memo.append(passes_subs)
	new_memo.append(branch)
	new_memo.append(memo_num)
	all_memos.append(new_memo)
	print(f"{memo} Done")

print("importing data to xlsx")
generate_xls(all_memos)
