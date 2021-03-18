import random
c=list(range(100000,999999))
random.shuffle(c)
for i in range (1,3):
    list1=['WA chennai', 'WB delhi',  'WC kerala', 'WD mumbai', 'WE banglore', 'WF vizag', 'WG hyd', 'WI madurai']
    b=random.randint(1,7)
    print("prize" + str(i))
    print(list1[b],c.pop())

print("prize 3")   
for i in range (1,13):
    list1=['WA chennai', 'WB america', 'WC Antartica', 'WD australia', 'WE godzilla', 'WF yolo', 'WG yoyo', 'WI dhg']
    b=random.randint(1,7)
    print(list1[b],c.pop())

print("Consolation")   
for i in range (1,13):
    list1=['WA chennai', 'WB america', 'WC Antartica', 'WD australia', 'WE godzilla', 'WF yolo', 'WG yoyo', 'WI dhg']
    b=random.randint(1,7)
    print(list1[b],c.pop())

print("prize 4")
for i in range(10):    
    print(random.randint(1000,9999))