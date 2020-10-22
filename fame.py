'''
    CS5002
    Michael Maquera
    Homework 1

    FLOWCHART
    START -> Get input from user in minutes -> calculate minutes to seconds ->
    ->calculate minutes to hours
    -> calculate hours to days -> print out each time on a seperate line -> end

    
'''

def main():
    #get user input
    fame_minutes = int(input("hello, how many fame minutes do you want? "))
    #calculate minutes
    fame_seconds = fame_minutes * 60
    #calculate hours
    fame_hours = fame_minutes / 60
    #calculate days
    fame_days = fame_hours / 24
    #print out each time amount in order
    print("great you'll be famous for ",fame_seconds ,'second(s)')
    print("great you'll be famous for {:0.3f}".format(fame_hours) ,'hour(s)')
    print("great you'll be famous for {:0.3f}".format(fame_days) ,'day(s)')
           

main()
    
