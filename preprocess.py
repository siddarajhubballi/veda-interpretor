fileRig = open('data/rigveda_exp_final.txt', 'r',encoding="utf8")
fileAtharva = open('data/atharvaveda_exp_final.txt', 'r',encoding="utf8")
fileSam = open('data/samveda_exp_final.txt', 'r',encoding="utf8")
fileYaju = open('data/yajurveda_exp_final.txt', 'r',encoding="utf8")

samaVeda = fileSam.read()
yajuVeda = fileYaju.read()
atharvaVeda = fileAtharva.read()
rigVeda = fileRig.read()

rig = open('processed_data/rigveda_exp_final.txt', 'w',encoding="utf8")
atharva = open('processed_data/atharvaveda_exp_final.txt', 'w',encoding="utf8")
sama = open('processed_data/samveda_exp_final.txt', 'w',encoding="utf8")
yaju = open('processed_data/yajurveda_exp_final.txt', 'w',encoding="utf8")

i=1
for line in rigVeda.splitlines():
    shloka = (str(i) + " :" + line + "\n")
    rig.write(shloka)
    i = i+1

i=1
for line in atharvaVeda.splitlines():
    shloka = (str(i) + " :" + line + "\n")
    atharva.write(shloka)
    i = i+1

i=1
for line in samaVeda.splitlines():
    shloka = (str(i) + " :" + line + "\n")
    sama.write(shloka)
    i = i+1

i=1
for line in yajuVeda.splitlines():
    shloka = (str(i) + " :" + line + "\n")
    yaju.write(shloka)
    i = i+1


fileRig.close()
fileAtharva.close()
fileSam.close()
fileYaju.close()

rig.close()
atharva.close()
sama.close()
yaju.close()


