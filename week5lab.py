#constants

LETTER_PRIORITY_FEE = 12.00
LETTER_STANDARD_FEE = 10.50
BOX_PRIORITY = 15.75
BOX_STANDARD = 13.75
ADD_BOX_PRIORITY = 1.25
ADD_BOX_STANDARD = 1.00
OUNCES_PER_POUND = 1
#inputs
type_of_package = input("enter the type of package (letter or box):")
type_of_service = input("enter type of service (standard or priority):")

#processing

if type_of_package == "letter":
    weight_of_package = int(input("enter type of weight(ounces)"))
    if type_of_service == "priority":
        fee = LETTER_PRIORITY_FEE

    elif type_of_service == "standard":

        fee = LETTER_STANDARD_FEE
    else:
     print("no package type")
     fee = 0


elif type_of_package == "box":
    weight_of_package = int(input("enter type of weight(pound)"))
    if type_of_service == "priority":
        if weight_of_package > 1:
         fee = ((weight_of_package - 1) * ADD_BOX_PRIORITY) + BOX_PRIORITY

    elif type_of_service == "standard":
     if weight_of_package > 1:
         fee = ((weight_of_package - 1) * ADD_BOX_STANDARD) + BOX_STANDARD

else:
    print("no package type")
    fee = 0

#outputs
print("The fee is €",fee,"for a package with")
print("type:", type_of_package)
print("service:", type_of_service)
print("ounces:", weight_of_package * 16)




#EX.2

#constants

STANDARD_PAY_RATE = 35
STANDARD_WORKING_WEEKS = 39
OVERTIME_PAY_RATE = 50





#inputs
hours_per_week = int(input("enter your hours worked per week:"))

