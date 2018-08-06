import sqlite3 
from sqlite3 import Error
import re
import os
import json 

home_location = os.getcwd()

class note:
	note_number = -1 
	note_value = [] 
	
	def __init__ ( self , number ):
		self.note_number = number 
	
		

def change_path ( user_name ) :
	path = 'C:\\users\\'+user_name+'\\appdata\\local\\packages'
	os.chdir(path)
	required = 'stickynotes'
	folder_name = ''
	for i in os.listdir():
		if required.lower() in i.lower():
			folder_name = i
			break
	os.chdir(folder_name+'\\localstate\\')
	return

def create_connection ( db_file ):
	try:
		connection = sqlite3.connect(db_file)
		return connection
	except Error as e:
		print(e)
	
	return None

def get_table_names ( db ) :
	cursor = db.cursor()
	cursor.execute("SELECT name from sqlite_master WHERE type='table';")
	tables = cursor.fetchall()
	final_values = []
	for i in tables:
		final_values.append(i[0])
	return final_values

def get_column_names ( db , table_name ) :
	cursor = db.execute("SELECT * from "+table_name+";")
	colnames = cursor.description
	final_values = []
	for i in colnames:
		final_values.append(i[0])
	return final_values
	
def get_column_contents ( db , table_name , col_name ):
	db.row_factory = lambda cursor , row: row[0]
	values = db.execute("SELECT "+col_name+" FROM "+table_name+";").fetchall()
	return values

def print_contents_notes ( temp_values ) :
	notes = []
	for i in range(len(temp_values)):
		temp_note = note ( i )
		final_values = [] 
		id_values = [m.start() for m in re.finditer('\\\id',temp_values[i])]
		id_values = [ int(x) for x in id_values ]
		for j in range(len(id_values)):
			j = int(j)
			new_line = temp_values[i].find(' ')
			if j+1 < len(id_values):
				string_value = temp_values[i][ id_values[j]+4 : id_values[j+1] ]
				string_value = string_value[string_value.find(' ')+1 : ]
				final_values.append(string_value)
			else:
				string_value = temp_values[i][id_values[j]+4 : ]
				string_value = string_value[string_value.find(' ')+1 : ]
				final_values.append(string_value)
		temp_note.note_value = final_values
		notes.append(temp_note)
	return notes
	
user_name = input("Enter user name\n")
change_path(user_name)
	
db = create_connection ( 'plum.sqlite' )

table_name = 'Note'

col_name = 'Text'

column_contents = get_column_contents ( db , table_name , col_name ) 
print()

values = print_contents_notes ( column_contents ) 

os.chdir ( home_location )

file_value = open ( 'json_value.txt' , 'w+' )

print("The contents of the notes are " )
for i in values:
	print ( "Note number :  " , i.note_number )
	print ( "Note contents : " )
	for j in i.note_value:
		print(j)
	json_value = json.dumps ( i.__dict__ ) 
	file_value.write(json_value)	
	print()
file_value.close()

