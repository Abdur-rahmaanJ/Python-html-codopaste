import csv

with open("file.csv","r") as f:
	reader = csv.reader(f)
	myList = list(reader)

print(myList)

x=0
y=0

syntax_list=[]
colours_list=[]
while x < len(myList):
	syntax_list.append(myList[y][0])
	colours_list.append(myList[y][1])
	x+=1
	y+=1

print(colours_list)
print(syntax_list)

txt = "j tgty aaa tyhty bbb yhtyh on rgr ccc tg it ejghri do"

x=0
y=0
while x<len(syntax_list):
	txt=""+txt.replace(syntax_list[y],'<span style ="color:'+colours_list[y]+';">'+syntax_list[y]+'</span>')
	x+=1
	y+=1

print(txt)
