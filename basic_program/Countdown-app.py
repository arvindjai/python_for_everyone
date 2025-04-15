from datetime import datetime

user_input = input("Enter Goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)
# print(input_list[0])
# print(input_list[1])
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_day = datetime.today()
time_till = deadline_date - today_day

print(f"Dear user! Time remaining for your goal: {goal} is {time_till} days")
