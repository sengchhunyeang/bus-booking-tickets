
# here below there are color 
COLOR_BLACK="\033[0;30m"
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_BROWN="\033[0;33m"
COLOR_BLUE="\033[0;34m"
END_COLOR="\033[0m"

print(f"{COLOR_BLUE}="*40)
print(f"{COLOR_GREEN} Bus Booking System {END_COLOR}".center(50))
print(f"{COLOR_BLUE}={END_COLOR}"*40)

# mytext=["1. Booking a Ticket","2. Cancel a Ticket","3. Show Available Seats","4. Exit"]

# for x in mytext:
#     print(x)
 
print("1. Booking a Ticket")
print("2. Cancel a Ticket")
print("3. Show Available Seats")
print("4. Exit")
print(f"{COLOR_BLUE}={END_COLOR}"*40)
# \t is a tab 
inputOption = input("Enter your chose :\t")

print("Input Option :",inputOption)


