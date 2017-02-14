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

fileX = open("repl.txt","r")
rvar = fileX.read()
fileX.close()

print(colours_list)
print(syntax_list)

#escape chars
# esc =    [   '\n',   '<',   '>',   '&']
# escRep = ['</br>','&lt;','&gt;','&amp']
# a=0
# b=0
# while a < len(esc):
# 	rvar=""+rvar.replace(esc[b],escRep[b])
# 	a+=1
# 	b+=1

#html formatting
x=0
y=0
while x<len(syntax_list):
	rvar=""+rvar.replace(syntax_list[y],'<span style ="color:'+colours_list[y]+';">'+syntax_list[y]+'</span>')
	x+=1
	y+=1

#print(rvar)

rvar=""+rvar.replace('\n','</br>')

beg = '<div style="background-color:tan;" ><p>'
end = '</p></div>'

fileY=open("replf.html","w+")
fileY.write(beg)
fileY.close()

fileZ=open("replf.html","a")
fileZ.write(rvar)
fileZ.write(end)
fileZ.flush()
fileZ.close()

