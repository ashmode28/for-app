sur_name = input("enter name: ")
middle_name = input("enter middle name: ")
first_name = input("enter first name: ")
age = int(input("input age:"))
if age <= 18:
    print("your are not allow to access this web. ")
else:
    password = input("enter password:")
    comfirm_password = input("enter comfirm:")
    if password != comfirm_password:
        password = input("enter password:")
        comfirm_password = input("enter comfirm:")
        if password != comfirm_password:
            password = input("enter password:")
            comfirm_password = input("enter comfirm:")
        else:
            print("your has sucessfully created")

    else:
         print("account has sucessfully created")


