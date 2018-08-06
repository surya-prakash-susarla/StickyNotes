import os
import json 

from send_mail import Mail
from db_contents import DatabaseHandler

home_location = os.getcwd()

TABLE_NAME = 'Note'
COL_NAME = 'Text'
DB_FILE = 'plum.sqlite'

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

	
user_name = input("Enter user name\n")
change_path(user_name)

db_connection = DatabaseHandler()

db = db_connection.create_connection ( DB_FILE )

column_contents = db_connection.get_column_contents ( db , TABLE_NAME , COL_NAME ) 

values = db_connection.convert_contents_notes ( column_contents ) 

string_values = '\n\n' 
for i in values: 
	string_values = string_values + 'Note : ' + str(i.note_number) + '\n'
	for j in i.note_value:
		string_values = string_values + j + '\n'
	string_values = string_values + '\n\n'

os.chdir ( home_location )

file_value = open ( 'json_value.txt' , 'w+' )

for i in values:
	json_value = json.dumps ( i.__dict__ ) 
	file_value.write(json_value)	
	
file_value.close()

sender = input("Enter sender mail id\n")
sender_password = input("Enter sender password id\n")
receiver = input("Enter receiver mail id\n")

#sending string value to mail 
mail_obj = Mail ( sender , sender_password , receiver )
mail_obj.send_mail ( string_values ) 

#JSON FILE CREATED IN CURRENT DIRECTORY , FILE NAME : 'json_value.txt'