
from graphics import *
import csv
import math

def main():
    while True:  #outer loop that circles until user enter N for “Do you want to select a new data file? Y/N”
        data_list=[]
        def load_csv(CSV_chosen):
            """
            This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
            YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
            """
            with open(CSV_chosen, 'r') as file:
                csvreader = csv.reader(file)
                header = next(csvreader)
                for row in csvreader:
                    data_list.append(row)
        
    #Task A
        airport_codes = {
            'LHR': 'London Heathrow',
            'MAD': 'Madrid Adolfo Suárez-Barajas',
            'CDG': 'Charles De Gaulle International',
            'IST': 'Istanbul Airport International',
            'AMS': 'Amsterdam Schiphol',
            'LIS': 'Lisbon Portela',
            'FRA': 'Frankfurt Main',
            'FCO': 'Rome Fiumicino',
            'MUC': 'Munich International',
            'BCN': 'Barcelona International'
        }

        #Getting a valid depature 3 letter city code
        def get_departure_city_code():
            """
           This function identifies when selected departure airport code input 
           is wrong length or 
           not one of the available codes
           When input is incorrect - prompts user for the correct format
            """
   
            code_validity=False
            while code_validity == False:
                city_input=input("Please enter the three letter airport code : ").strip()#strip remove witespaces between code

                if len(city_input) !=3:#Check if it exactly 3 character city code
                    print("Wrong code length - please enter a three-letter city code")
                else:
                    city_input=city_input.upper()

                    if city_input in airport_codes:
                        code_validity = True
                        return city_input
                    else:
                        print('Invalid city code.Please Enter valid city code')


        def get_year_validity():
            """
            This function identifies when year input is the wrong data type or range 
            When input is incorrect - prompts user for the correct format and range
            """
            year_valid=False
            while year_valid ==False:
                year_input=input("Please enter the required year in the format YYYY : ").strip()#strip remove witespaces between year typed
                if len(year_input) !=4:    #Checking for the year with 4  characters
                    print("Wrong code length - Please enter a four-digit year value")
                else:
                    try:
                        year=int(year_input)
                        
                        #check year is between 2000 and 2025
                        if year < 2000 or year > 2025:
                            print("Out of range - Please enter a value from 2000 to 2025")
                        else:
                            year_valid =True
                            return year
                    except:
                        print("Wrong data type - Please enter a four-digit year value")

        #TaskB
        def count_total_flights():     #1.The total number of flights from this airport
            return len(data_list)      

        def count_flights_terminal_2(): 
            """
            2.This chechecks the total number of flights departing 
            from Terminal 2.
            """
            terminal_2_count = 0
            for flights in data_list:
                if flights[8] == '2':  #checking the flights which depature from terminal 2
                    terminal_2_count +=1
            return terminal_2_count

        def count_flights_short():        
            """ 
            3.This checks The total number of departures of flights
            that are under 600 miles
            """
            count_short_flights = 0      
            for flights in data_list:
                distance = int(flights[5]) 
                if distance<600:       
                    count_short_flights +=1
            return count_short_flights

        def  count_flights_af():     #4.The total number of departure flights by Air France aircraft.
            count_af=0
            
            for flights in data_list:
                flight_code=flights[1]   #Taking the fight name
                flight_name=flight_code[:2]    #Taking first 2 letters of the flight code
                if flight_name =='AF':
                    count_af+=1
            return count_af

        def count_flights_temp():   #5.The total number of flights departing in temperatures below 15C
            count_temp = 0
            
            for flights in data_list:
                flights_t=flights[10] 
                flights_temp=flights_t[:2] #Taking first 2 strings
                flights_tempint=int(flights_temp)
                if flights_tempint<15:
                    count_temp +=1
            return count_temp

        def flights_avgba():     
            """
            6.The average number of British Airways departures
             per hour (rounded to two decimal places)
             """

            count_ba=0           #ba-british Airway
            for flights in data_list:
                flights_code=flights[1]
                flights_name=flights_code[:2] #Taking first 2 strings
                if flights_name =='BA':   
                    count_ba +=1
            ba_avg=count_ba/12
            return round(ba_avg,2)    

        def percentage_ba_flight():    
            """
           7.This function takes the percentage of total 
           departures that are British Airways aircraft 
            (rounded to two decimal places)
            """   

            count_ba =0
            total_flights=len(data_list)
            for flights in data_list:
                flights_n=flights[1]
                flights_name=flights_n[:2] #Taking first 2 strings
                if flights_name =='BA':   
                    count_ba +=1
            ba_percentage=(count_ba/total_flights)*100
            return round(ba_percentage,2) #rounding the value to second decimal place

        def percentage_af_delay_flights(): 
            """8.This finds The percentage of Air France flights with 
            a delayed departure by taking first two leters of AF from csv file
             """

            count_total_af=0  #total  Air FranceAirway flights af-air France flight
            count_delay=0    #delayed Air france airway flights

            for flights in data_list:#total air France Airway flights
                flights_n=flights[1]
                flights_name=flights_n[:2] #Taking first 2 strings of airline
                if flights_name =='AF':   #checking the airline is AF
                    count_total_af +=1

                    #finding delayed flights
                    flights_scheduled=flights[2] #Taking the scheduled time
                    flights_delayed=flights[3]   #Taking the 
                    if flights_scheduled != flights_delayed:
                        count_delay +=1
            
            #Calculating percentage
            percentage_afdelay_flights=(count_delay/count_total_af)*100
            return round(percentage_afdelay_flights,2) #rounding the percentage to second decimal place


        def count_rain_hours(): 
            """This finds the total number of hours of rain in 
               the twelve hours (rain values are recorded once every hour) 
               by taking the hours and their respective weather  """

            rain_hours_count=0
            previous_hour="" #prevents the duplication of pervious hour

            for flights in data_list:
                weather=flights[10]
                if 'rain' in weather:     
                    depature_time=flights[2] 
                    depature_hour=depature_time[:2]
                    if depature_hour != previous_hour:
                        rain_hours_count+=1
                        previous_hour= depature_hour
            return rain_hours_count


        def full_name_least_des():    
            """#10.This function gives the full name of the least
             common destination (or names if more than one)."""

            departure_dictionary={}  #count of airports that flights landed stored here
            for flights in data_list:
                final_destination=flights[4] #taking the final destination from data
                if final_destination in departure_dictionary:
                    departure_dictionary[final_destination]+=1
                else:
                    departure_dictionary[final_destination]=1
            
            #least count calculating
            least_visited_destination = min(departure_dictionary, key=departure_dictionary.get)
            least_visited_destination_final = airport_codes.get(least_visited_destination)
            return least_visited_destination_final
            
            

          

        airport = get_departure_city_code()   #Get validated airport code
        year_chosen = get_year_validity()   # Get validated year
        selected_data_file = airport + str(year_chosen) + ".csv"  # Build filename
        full_airport_name = airport_codes[airport] # Get full airport name

        # Display output
        load_csv(selected_data_file)#calls the function "load_csv" sending the variable 'selected_data_file" as a parameter 

        #call
        total_flights_count = count_total_flights()
        terminal_2 = count_flights_terminal_2()
        short_distance_flights = count_flights_short()
        af_flights = count_flights_af()
        temp_flights = count_flights_temp()
        ba_avg = flights_avgba()
        ba_percentage = percentage_ba_flight()
        af_delay = percentage_af_delay_flights()
        rain_hours = count_rain_hours()
        least_dest = full_name_least_des()

        #display the output 
        print("*" * 80 )
        print(f"{selected_data_file} selected - Planes departing {full_airport_name} {year_chosen}")
        print("*" * 80)   

        print(f"The total number of flights from this airport was {total_flights_count}")
        print(f"The total number of flights departing Terminal Two was {terminal_2}")
        print(f"The total number of departures on flights under 600 miles was {short_distance_flights}")
        print(f"There were {af_flights} Air France flights from this airport")
        print(f"There were {temp_flights} flights departing in temperatures below 15 degrees")
        print(f"There was an average of {ba_avg} British Airways flights per hour from this airport")
        print(f"British Airways planes made up {ba_percentage}% of all departures")
        print(f"{af_delay}% of Air France departures were delayed")
        print(f"There were {rain_hours} hours in which rain fell")
        print(f"The least common destinations are {least_dest}")
        print()
        print("="*80)


        #Task C. Save Results as a Text File
        def results():
            with open("results.txt","a") as f:
                f.write("*" * 80 +"\n")
                f.write(f"{selected_data_file} selected - Planes departing {full_airport_name} {year_chosen}\n")
                f.write("*" * 80+"\n")   
                f.write(f"The total number of flights from this airport was {total_flights_count}\n")
                f.write(f"The total number of flights departing Terminal Two was {terminal_2}\n")
                f.write(f"The total number of departures on flights under 600 miles was {short_distance_flights}\n")
                f.write(f"There were {af_flights} Air France flights from this airport\n")
                f.write(f"There were {temp_flights} flights departing in temperatures below 15 degrees\n")
                f.write(f"There was an average of {ba_avg} British Airways flights per hour from this airport\n")
                f.write(f"British Airways planes made up {ba_percentage}% of all departures\n")
                f.write(f"{af_delay}% of Air France departures were delayed \n")
                f.write(f"There were {rain_hours} hours in which rain fell\n")
                f.write(f"The least common destinations are {least_dest}\n")
                f.write(f"\n")

        results()
        #Task D-Histogram
        airline_codes_name = {
                "BA": "British Airways",
                "AF": "Air France",
                "AY": "Finnair",
                "KL": "KLM",
                "SK": "Scandinavian Airlines",
                "TP": "TAP Air Portugal",   
                "TK": "Turkish Airlines",
                "W6": "Wizz Air",
                "U2": "easyJet",
                "FR": "Ryanair",
                "A3": "Aegean Airlines",
                "SN": "Brussels Airlines",
                "EK": "Emirates",
                "QR": "Qatar Airways",
                "IB": "Iberia",
                "LH": "Lufthansa"
            }
        #Enter a two-character Airline code to plot a histogram:
        def get_Airline_code():  
            """
            This function gets two character Airline code to plot a histogram 
            and verify that the airline code entered is one of the valid airlines

            """ 
            while True:
                get_airline_input = input("Enter a two-character Airline code to plot a histogram: ").upper().strip()#
                
                if len(get_airline_input) != 2:
                    print("Enter the two-character Airline code to plot a histogram: ")
                    continue 

                if get_airline_input in airline_codes_name:
                    return get_airline_input  # Valid code 
                else:
                    print("Unavailable Airline code please try again")
               
                       

       
        def get_hourly_airline_data(airline_code):
            """ The histogram should show the total 
                 number of departing flights for the selected
                 airline, for eachhour of the twelve-hour survey"""
            hour_count=[0]*12

            for flights in data_list:
                departure_time=flights[2]
                departure_hour=departure_time[:2]
                departure_hour_int=int(departure_hour)
                
                airline=flights[1]
                flight_code=airline[0:2] #takes only the flight code

                if flight_code == airline_code:
                    hour_count[departure_hour_int]+=1
            return hour_count

        #graphics.py
        
        def draw_histogram(hour_count, airline_code, airport_name,year):  
            """This function creates a pop up window of histogram
            refernce:
                Zelle, J.M. (2010). "Python Programming: An Introduction to Computer Science" by John Zelle,
                published by Franklin, Beedle & Associates
            """

            airline_full_name = airline_codes_name[airline_code]

            #The popup window we gonna open 
            win=GraphWin("Histogram ",700,500)   #title,width,heght 
            win.setBackground("white")

            #title at the top of the graph
            top_title=(f"Departures by hour for {airline_full_name} from {airport_name} {year}")
            top_title=Text(Point(350,20),top_title)   #(Point(x,y))-Find the position
            top_title.setSize(11)
            top_title.setStyle("bold")
            top_title.setTextColor("navy")
            top_title.draw(win)
            
            #Checking which hour got the highest no.of flights of particular airline
            maximum_flights = max(hour_count) # Find highest value
            if maximum_flights == 0:
               maximum_flights = 1 # Avoid dividing by zero
            

            #bar scaling
            bar_height= 25
            bar_gaps=10
            top_bar=40
            margin_start=100
            #scaling the bar
            max_bar_width = 500 # Maximum pixels available for bars
            scale_bars = max_bar_width/maximum_flights
        
            #y axis Text
            Y_axis_represents=Text(Point(40,200),"HOURS\n 00:00 \n  to \n 12:00")
            Y_axis_represents.setSize(11)
            Y_axis_represents.setStyle("bold")
            Y_axis_represents.draw(win)

            # Draw Y-axis margin line 
            y_axis_line = Line(Point(margin_start, top_bar), 
                            Point(margin_start, top_bar + (12*(bar_height + bar_gaps)-10)))
            y_axis_line.setWidth(2)
            y_axis_line.setOutline("black")
            y_axis_line.draw(win)



            for hour in range(12):# Draw bars and labels for each hour
                flights_in_this_hour=hour_count[hour]
                
                y_axis_label_positions=top_bar+(hour*(bar_height+bar_gaps)) # positioning of y axis labels correctly

                hour_text = f"{hour:02d}"  #gives hours  00 01 02 ......
                hour_labels = Text(Point(90, y_axis_label_positions + bar_height/2), hour_text)
                hour_labels.setSize(9)
                hour_labels.setStyle("bold")
                hour_labels.draw(win)       

                
                
                # Calculate bar length
                bar_length = flights_in_this_hour * scale_bars
                

                # Horizontal bars looks
                horizontal_bar = Rectangle(Point(margin_start, y_axis_label_positions), 
                            Point(margin_start + bar_length, y_axis_label_positions + bar_height))
                horizontal_bar.setFill("lightgreen")
                horizontal_bar.setOutline("darkgreen")
                horizontal_bar.setWidth(1)
                horizontal_bar.draw(win)
                
                # Draw count number at end of bar
                if flights_in_this_hour > 0:
                    count_label = Text(Point(margin_start + bar_length + 20, y_axis_label_positions + bar_height/2), 
                                    str(flights_in_this_hour))
                    count_label.setSize(9)
                    count_label.setStyle("bold")
                    count_label.draw(win)
            
        
            # Wait for click and close
            """This prevents the getting a graphic error if user
             click on close button on the pop up window"""
            try:   
                win.getMouse()
                win.close()
            except GraphicsError:
                pass

        airline_code = get_Airline_code()
        airline_hourly_counts = get_hourly_airline_data(airline_code)
        draw_histogram(airline_hourly_counts, airline_code, full_airport_name, year_chosen)


            #Task E
        while True: #inner loop which loops until the correct input given
            New_data_file=input("Do you want to select a new data file? Y/N: ").strip().upper()    
            #remove unwanted whitespacesand makes letters capitalise    
            if New_data_file =="Y":
                print()
                break  # Break inner loop, continue outer loop
            elif New_data_file == 'N':
                print("Thank you. End of run")
                return  #ends the program 
            else:
                print("invalid input... Please enter (Y/N)")

                
if __name__ == "__main__":
   main()
    




            













  






