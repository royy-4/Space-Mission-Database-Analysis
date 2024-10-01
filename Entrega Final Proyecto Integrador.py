#import libraries to format / read data and generate plots
import datetime
import pandas as pd
import matplotlib.pyplot as plt 

#read csv file data using pandas library
def read_csv_file(file_name):
    
    csv_data = pd.read_csv(file_name)
    
    return csv_data


#takes the data frame an filters the data by sorting each mission per country
 
def location_filter(data_frame):
    
    unique_countries = []

    for country in data_frame['Location']:

        if country not in unique_countries:
            unique_countries.append(country)


    countryFrecuency = [0] * len(unique_countries) #initialize a list with value 0, and multiply it by the number of countries in the unique countries list
    #eg [0] * 5 = [0,0,0,0,0], repeat the initial value n times in a new list

   
    for country in data_frame['Location']:

        index = unique_countries.index(country)
        countryFrecuency[index] += 1

    plt.bar(unique_countries,countryFrecuency,tick_label = unique_countries,color = 'blue')
    plt.xlabel('Countries')
    plt.ylabel('Mission Frecuency')
    plt.title('MISSION QUANTITY PER COUNTRY')


    plt.show()

    
#filters the data depending on the status of the mission

def mission_filter(data_frame):

    #0 = failed missions ; 1 = successfull missions, the original website where the csv was downloaded from indicated these values' meaning as such

    mission_status = [0,0] #[0] for failed missions, [1] for successfull missions

    for status in data_frame['MissionStatus']:

        if status == 1:
            mission_status[1] += 1
        
        elif status == 0:
            mission_status[0] += 1
        
        else:
            continue

    plt.bar(['Failed missions', 'Successful missions'],mission_status, color = 'green')
    plt.xlabel('Mission Status')
    plt.ylabel('Total quantity')
    plt.title('TOTAL FAILED AND SUCCESSFULL MISSIONS')   
    
    plt.show()


#filter the data depending on the status of the rocket

def rocket_filter(data_frame):
    
    rocket_status_values = []
    
    for rocket_status in data_frame['RocketStatus']:

        if rocket_status not in rocket_status_values:
            rocket_status_values.append(rocket_status)
    
    status_frecuency = [0] * len(rocket_status_values) #initialize a list with 0, with an index for each unique rocket status value

    for rocket_status in data_frame['RocketStatus']:

        index = rocket_status_values.index(rocket_status)
        status_frecuency[index] += 1


    plt.bar(rocket_status_values,status_frecuency, tick_label = rocket_status_values, color = 'yellow' )
    plt.xlabel('Rocket Status')
    plt.ylabel('Total quantity')
    plt.title('CURRENT ROCKET STATUS')

    plt.show()
  

#filter the data based on the unique launch date (taking into account year and time) for each mission
def date_filter(data_frame):


    #ZOOMING ON THE PLOT IS NECESSARY TO VIEW THE DATA PROPERLY, DUE TO THE AMOUNT OF UNIQUE LAUNCH DATES


    data_frame['Date'] = data_frame['Year'].astype(str) + data_frame['Time'] #create a new column that combines the year and time columns

    
    unique_dates = []

    for date in data_frame['Date']:

        if date not in unique_dates:
            unique_dates.append(date)

    
    date_frecuency = [0] * len(unique_dates)

    for date in data_frame['Date']:

        index = unique_dates.index(date)
        date_frecuency[index] += 1

    
    plt.bar(unique_dates,date_frecuency, tick_label = unique_dates, color = 'purple')
    plt.xlabel('Launch dates')
    plt.ylabel('Date frecuency')
    plt.title('FRECUENCY OF LAUNCH DATES')

    plt.show()



def main():

    file = 'spaceMissions1.csv'
    data = read_csv_file(file)
    

    print("1.Filter by country\n2.Filter by mission status\n3.Filter by rocket status\n4.Filter by launch date\n5.Exit\n6.View data frame")

    user_input = input("\nChoose how you wish to visualize the data (Enter a number)\n").casefold().strip()

    match user_input:
        case "1":
            #mission location function
            location_filter(data)
        case "2":
            #mission status function
            mission_filter(data)
        case "3":
            #rocket status function
            rocket_filter(data)
        case "4":
            #launch year function
            print("Manual zooming on the plot is required for proper data visualization\n")
            date_filter(data)
        case "5":
            exit()
        case "6":
            print(data)
        case _:
            print("Please enter a valid option\n")






if __name__ == "__main__":
    main()