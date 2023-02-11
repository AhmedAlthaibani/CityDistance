from geopy.distance import geodesic 

new_york = (40.66, 73.94)
los_angelas = (34.02, 118.41)
chicago = (41.84, 87.68)
houston = (29.79, 95.39)
phoenix = (33.57, 112.09)
philadelphia = (40.01, 75.13)
san_antonio = (29.46, 98.52)
san_diego = (32.81, 117.14)
dallas = (32.79, 96.77)
san_jose = (37.30, 121.81)

def greetingMessage():
    print("Welcome to Ahmed's City Distance Calculator! Please enter your name!")
    name = input()
    print("Hi " + name + "!") 
    print("You'll be given 10 of the most populated U.S Cities to choose from! Let's get started!")
    
def getCityDistance(city1,city2,choice1,choice2):
    print("Please select your first city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    choice1 = input()
    if choice1 == ("1"):
        city1 = (40.66, 73.94)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("2"):
        city1 = (34.02, 118.41)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("3"):
        city1 = (41.84, 87.68)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("4"):
        city1 = (29.79, 95.39)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("5"):
        city1 = (33.57, 112.09)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("6"):
        city1 = (40.01, 75.13)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("7"):
        city1 = (29.46, 98.52)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("8"):
        city1 = (32.81, 117.14)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")    
    if choice1 == ("9"):
        city1 = (32.79, 96.77)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    if choice1 == ("10"):
        city1 = (37.30, 121.81)
        print("Now select your second city!\n1. NYC\n2. LA\n3. Chicago\n4. Houston\n5. Phoenix\n6. Philadelphia\n7. San Antonio\n8. San Diego\n9. Dallas\n10. San Jose")
    choice2 = input()
    if choice2 == ("1"):
        city2 = (40.66, 73.94)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")        
    if choice2 == ("2"):
        city2 = (34.02, 118.41)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("3"):
        city2 = (41.84, 87.68)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("4"):
        city2 = (29.79, 95.39)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("5"):
        city2 = (33.57, 112.09)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("6"):
        city2 = (40.01, 75.13)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("7"):
        city2 = (29.46, 98.52)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("8"):
        city2 = (32.81, 117.14)  
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("9"):
        city2 = (32.79, 96.77)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")    
    if choice2 == ("10"):
        city2 = (37.30, 121.81)
        print(geodesic(city1,city2).miles)
        print("The above number is the distance between the cities you chose in miles!")        
    return city1,city2,choice1,choice2
    
city1 = getCityDistance
city2 = getCityDistance
choice1 = getCityDistance
choice2 = getCityDistance
greetingMessage()
repeat = True
while repeat == True:
    getCityDistance(city1,city2,choice1,choice2)
    print("Would you like to keep calculating?")
    response = input()
    if response == "Yes":
        repeat = True
    elif response == "No":
        break
    
