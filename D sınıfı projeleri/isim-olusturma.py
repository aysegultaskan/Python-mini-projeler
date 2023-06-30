import random

def isim_sec():
    ilk_ismi = ["Jeon", "Kim", "Park", "Lee", "Min", "Jung"]
    ikinci_isim = [" Seok", " Nam", " Ji", " Tae", " Jung", " Yoon"," Ho", " Soo", " Je"]
    son_isim = ["Jin", "Joon", "Min", "Hyung", "Kook", "Gi", "Seok", "Hyun", "Hoon"]
    return "{}{}{}". format(random.choice(ilk_ismi), random.choice(ikinci_isim), random.choice(son_isim))
 
for i in range(5):
    print(isim_sec())
     

