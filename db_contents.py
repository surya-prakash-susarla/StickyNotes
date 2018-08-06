import sqlite3 
from sqlite3 import Error
import re
import os

class note:
	note_number = -1 
	note_value = [] 
	
	def __init__ ( self , number ):
		self.note_number = number 

class DatabaseHandler:

	def create_connection ( self , db_file ):
		try:
			connection = sqlite3.connect(db_file)
			return connection
		except Error as e:
			print(e)
		
		return None

	def get_column_contents ( self , db , table_name , col_name ):
		db.row_factory = lambda cursor , row: row[0]
		values = db.execute("SELECT "+col_name+" FROM "+table_name+";").fetchall()
		return values

	def convert_contents_notes ( self , temp_values ) :
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
