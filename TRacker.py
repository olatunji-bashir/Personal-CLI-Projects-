from pickle import TRUE
import sched


# create a list to store activities

current_time = []


def Add_activities():
    add_Activity_list = []

    print("Adding an Activities.....")

    # ask for input to store activity data
    Activity_name = "Activity name: " + input("Enter Activity_name: ")
    Activity_Start_time = "Activity start time: " + input("Enter Activity start time: ")
    Activity_end_time = "Activity end time: " + input("Enter Activity_end_time: ")
    Activity_status = []

    # Append Activities to the empty list 
    add_Activity_list.append([Activity_name, Activity_Start_time, Activity_end_time, Activity_status])

    # saving activities to external file
    Activity_file = open("Activitylist.txt", "n")
    for activity in add_Activity_list:
        Activity_file.write(",".join(activity) + "\n")
    Activity_file.close()

    return Add_activities


def Activity_list():
    list = []
    Task_list = list.append(Add_activities())
    print(Task_list)
    return Activity_list


# Tracks the status of the activity
def start_activity():
    for Activity in Activity_list:
        if Activity.Activity_status == "No" or "":
            Activity.Activity_status = False
        else:
            Activity.Activity_status = True
    
    return start_activity() 
        


def To_do_task():
    for Activity in Activity_list:
        if Activity.Activity_Start_time <= current_time and start_activity == True:
            print("Activity is still pending.........")
        else:
            print("")
    return To_do_task


def Task_in_progress():
    for Activity in Activity_list:
        if Activity.Activity_Start_time < current_time and start_activity == True:
            print("Task currently in progress........")
        else:
            print("Task still pending........")

