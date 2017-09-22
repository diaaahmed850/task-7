import csv
name_form=[]
email_form=[]
mobile_form=[]
uni_form=[]
major_form=[]
form={'name':name_form,
      'email':email_form,
      'mobile':mobile_form,
      'university':uni_form,
      'major':major_form

}
dic={}
user_input=""
user_index=0
dic.update({user_index:[]})
dic[0].append(50)
print(dic)
while 1:
    user_input=input()
    if user_input == "stop":
        break
    else:
        if user_index == 0:
            form['name'].append(user_input)
            user_index+=1
        elif user_index == 1:
            form['email'].append(user_input)
            user_index += 1
        elif user_index == 2:
            form['mobile'].append(user_input)
            user_index += 1
        elif user_index == 3:
            form['university'].append(user_input)
            user_index += 1
        elif user_index == 4:
            form['major'].append(user_input)
            user_index=0


with open ("form.csv","a") as f:
    csv_app=csv.writer(f)
    csv_app.writerow(form.keys())
    for n in form.values():
        csv_app.writerow(n)




