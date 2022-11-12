list_id = []
amnt_employee = int(input("Enter the amount of employee: "))
for i in range(amnt_employee):
    new_id = int(input(f"Enter the ID for {i} employee: "))
    list_id.append(new_id)
search_id = int(input("What ID searching?: "))
flag = False
for i in list_id:
    if i == search_id:
        flag = True
if flag:
    print("Employer is working now!")
else:
    print("Employer is not working now!")
