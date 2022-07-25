print("*****EVENT BOOKING MANAGER******")


def main():
    
    # initializing event list
    events_list = []
    people_attending_event = []


    choice = 0
    while choice != 4:
        print("*****EVENT BOOKING MANAGER******")
        print("1) Add an Event")
        print("2) Events Available for Booking")
        print("3) Display all Event Attendees")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding an Event.....")
            nEvent = input("Enter Event Name: ")
            nLocation = input("Enter Event Location: ")
            nDate = input("Enter Event Date: ")
            events_list.append([nEvent, nLocation, nDate])
        
        
        elif choice == 2:
            print("LOADING Events Available for Booking.....")
            keyword = input("Enter Event Search term: ")
            for event in events_list:
                if keyword in event:   
                    print(event)
                    
                    # initialize the event booking process
                    # though the use of an if statement1

                    
                    Event_booking = input("Do you want to book this event? (yes or no): ")
                    if Event_booking == ("no"):
                        print("Event not booked")
                        #return main
                    else:
                        print("1). Check PNR status")
                        print("2). Ticket Reservation")
                        # initialize the options above 
                        option = int(input("\nEnter your option: "))

                        # For now we just print PNR is active
                        if option == 1:
                            print("Your PNR status is active")

                            

                        # Getting the information for Ticket reservations
                        elif option == 2:
                            
                            # people variable gets the number of ticket 
                            people = int(input("\nEnter no. of Tickets you want: "))
                            
                            # creat empty list representing the name, age, and sex of the
                            # attendees.
                            name = []
                            age = []
                            sex = []
                            #no
                            people_attending_event.append([name])
                            for persons in range(people):
                                booking_name = input("\nName: ")
                                name.append(booking_name)
                                booking_age = input("\nAge: ")
                                age.append(booking_age)
                                booking_sex = input("\nSex: ")
                                sex.append(booking_sex)
                            
                            # Ask if any information was forgoting so as to rewrite the information given
                            # Else we print the information given.
                            Event_booking = input("\nDid you forget any information? yes/no: ")
                            if Event_booking in ("y", "yes", "YES", "Y"):
                                Event_booking = ("yes")
                            else:
                                x = 0
                                print("\nTotal Ticket: ", people)
                                for persons in range(1, people + 1):
                                    print("Ticket: ", persons)
                                    print("Name: ", name[x])
                                    print("Age: ", age[x])
                                    print("Sex: ", sex[x])
                                    x += 1
                                #return main
                
                        
        
        elif choice == 3:
            print("Displaying people attending event......")
            for i in range(len(people_attending_event)):
                print(people_attending_event[i])
        
        elif choice == 4:
            print("Closing Application......")
    
    print("Application closed")






















if __name__ == "__main__":
    main()








