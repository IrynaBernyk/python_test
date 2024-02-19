fruit1= ['rottenKiwi', 'strawberry', 'mango', 'rottenBanana', 'tomato', 'apple']

fruit2= ['kiwi', 'strawberry', 'mango', 'banana', 'tomato', 'apple']

fruit1_lower = fruit1.lower()



rotten = fruit1_lower.find ("rotten")
print (rotten)

for rotten in fruit1_lower():
    edited_fruit=fruit1_lower.replace("rotten", "")


print (edited_fruit)

