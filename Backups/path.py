import os


path = 'C:\\users\\surya prakash\\appdata\\local\\packages'

os.chdir(path)

required = 'StickyNotes'

folder_name = ''

for i in os.listdir():
	#print(i)
	if required.lower() in i.lower():
		folder_name = i
		break

print("value = " , folder_name )
os.chdir(folder_name+'\\localstate\\')

print(os.listdir())
