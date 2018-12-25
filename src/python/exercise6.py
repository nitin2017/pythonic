# EXERCISE --- WATCH COC
# ASK USER NAME AND AGE
# IF USER's name starts with 'a' or 'A' and age is above 10 then 
# Print "You can watch coco movie"
# else print "sorry you cannot watch coc movie"

name  =  input("Enter your name :-  ").strip()
age  =  int(input("Enter your age :-  ").strip())
if ((name[0:1]=='a' or name[0:1] =='A') and age >10):
    print("You can watch coco movie")
else:
    print("Sorry you cannot watch coco movie")

   
