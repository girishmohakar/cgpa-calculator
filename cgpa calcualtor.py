math_credit = 3
edc_credit = 3
edclab_credit = 1
de_credit = 3                                 
ufv_credit = 3
oe_credit = 2                                             
mdm_credit = 2
esd_credit = 2
locsm_credit = 1
cep_credit = 2
delabs_credit = 1

math_marks = int(input("how much total marks did you get in maths "))
edc_marks = int(input("how much total marks did you get in edc "))
edclab_marks = int(input("how much total marks did you get in edclab "))
de_marks = int(input("how much total marks did you get in de "))                                         
ufv_marks = int(input("how much total marks did you get in ufv "))
oe_marks = int(input("how much total marks did you get in oe "))
mdm_marks = int(input("how much total marks did you get in mdm "))
esd_marks = int(input("how much total marks did you get in esd "))
locsm_marks = int(input("how much total marks did you get in locsm "))
cep_marks = int(input("how much total marks did you get in cep "))
delabs_marks = int(input("how much total marks did you get in delabs "))

if math_marks <= 100:
    math_marks = (math_marks * 10)/100
else:    
    print("please enter valid marks")

if edc_marks <= 100:
    edc_marks = (edc_marks * 10)/100
else:    
    print("please enter valid marks")

if edclab_marks <= 100:
    edclab_marks = (edclab_marks * 10)/100
else:    
    print("please enter valid marks")    

if de_marks  <= 100:
    de_marks  = (de_marks * 10)/100
else:    
    print("please enter valid marks")

if ufv_marks <= 100:
    ufv_marks = (ufv_marks * 10)/100
else:    
    print("please enter valid marks")    

if oe_marks <= 100:
    oe_marks = (oe_marks * 10)/100
else:    
    print("please enter valid marks")

if mdm_marks  <= 100:
    mdm_marks  = (mdm_marks  * 10)/100
else:    
    print("please enter valid marks")    

if esd_marks <= 100:
    esd_marks = (esd_marks * 10)/100
else:    
    print("please enter valid marks")    

if locsm_marks <= 100:
    locsm_marks = (locsm_marks * 10)/100
else:    
    print("please enter valid marks")    

if cep_marks <= 100:
    cep_marks = (cep_marks * 10)/100
else:    
    print("please enter valid marks")    

if delabs_marks <= 100:
    delabs_marks = (delabs_marks * 10)/100
else:    
    print("please enter valid marks")

cgpa = ((math_credit * math_marks) + (edc_credit * edc_marks) + (edclab_credit * edclab_marks) + (de_credit * de_marks) + (ufv_credit * ufv_marks) + (oe_credit * oe_marks) + (mdm_credit * mdm_marks ) + (esd_credit * esd_marks) + (locsm_credit * locsm_marks) + (cep_credit * cep_marks ) + (delabs_credit * delabs_marks))/23

print(f'congratulations! your sgpa of this semister is {cgpa}, work harder next time')