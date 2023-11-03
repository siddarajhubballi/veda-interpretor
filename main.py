
def giveShloka(choice,id):
    veda="processed_data/"
    if(choice == 1):
        veda = veda + "rigveda_exp_final.txt"
    elif(choice == 2):
        veda = veda + "samveda_exp_final.txt"
    elif(choice == 3):
        veda = veda + "atharvaveda_exp_final.txt"
    else :
        veda = veda + "yajurveda_exp_final.txt"
    
    f = open(veda, "r", encoding="utf8")
    for i in range(1,id):
        sentence = f.readline()
    sentence = f.readline()
    return sentence


choice = int(input("MENU :\n1. Rig Veda\n2. Sama Veda\n3. Atharva Veda\n4. Yajur Veda\nEnter your choice : "))
print(choice)
id = int(input("Enter Sholka id : "))
print(id)

print(giveShloka(choice,id))
