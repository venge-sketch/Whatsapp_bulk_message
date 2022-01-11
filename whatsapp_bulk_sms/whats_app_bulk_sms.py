import csv
import pywhatkit
file = open("contacts.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows[5][0], rows[5][-3])

clean_names = []
clean_numbers = []
def clean_csv():
    for items in rows:
        clean_names.append(items[0])
        clean_numbers.append(items[-3])
    make_dict()
    

contact_list=[]

def make_dict():
    
    for i in range(0,len(clean_names)):
        dic = {}
        dic["name"] = clean_names[i]  
        dic["phone_number"] = clean_numbers[i]  

        contact_list.append(dic)
    
    

    print(contact_list )

def send_message():
    for index, contacts in enumerate(contact_list,1):
        pywhatkit.sendwhatmsg(contacts["phone_number"], f"Hi, {contacts['name']} this message is from an automated python bot. Just checking if it works. Happy new year!! :)", 23, 22+index )
       
        pass


clean_csv()
send_message()
# file.close()