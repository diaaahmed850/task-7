import csv
form={}
header=['name','email','mobile','university','major']
user_input=""
user_index=0
user_counter=1
while 1:
    user_input=input()
    if user_input == "stop":
        break
    else:
        if user_counter==1:
            form.update({user_index: []})
        form[user_index].append(user_input)
        user_counter+=1
        if user_counter==6:
            user_counter=1
            user_index+=1

with open ("form.csv","w",newline="") as f:
    csv_app=csv.writer(f)
    csv_app.writerow(header)
    for n in form.values():
        csv_app.writerow(n)





