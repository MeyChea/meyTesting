class Booking:
    def __init__(self):
        self.data = {"09:00am":"False", "10:00am":"True", "11:00am":"True", "12:00pm":"False",
                     "01:00pm":"True", "02:00pm":"True", "03:00pm":"True", "04:00pm":"True"}
    # Checking if time is available or not
    def printData(self, input,name):
        if self.data[input]=="True":
            print (name + " has successfully booked at " + input)
        else:
            print("Time is unavialable")

        # for i in self.data:
        #     if i == input:
        #         print(i + ' is not available')
        #     elif i != input:
        #         print(i + ' is available')


# Time that already booked by the customer
b = Booking()
# b.printData("09:00am")
# b.printData("12:00pm")

name = input("What is your name?")
time = input("When do you want to book your time?")
print("Name:", name, "  " "Booking time:", time)
b.printData(time,name)



#
#
# def timeAvailable(time_req: enumerate) -> bool:
#     '''return true if booking is taken'''
#
#
# global reserve_list
# reserve_booking = []
# for t in reserve_list:
#     reserve_booking.append(t.book)
# if (time not in reserve_booking):
#     raise True
#
# # def cancleTimeBooking(time:enumerate):
# #     for t in