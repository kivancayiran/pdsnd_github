import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

bikesharecities = ['chicago', 'new york city', 'washington']
bikesharemonths = ["january", "february", "march", "april", "may", "june", "all"]
bikesharedays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Could you please choose one of the following cities? \nChicago, \nNew York City, \nWashington\n").lower()
        if city in bikesharecities:
            break
        else:
            print("The city choosen by you is not in the list. Please choose on of the folloring cities: Chicago, New York or Washington\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Could you please choose one of the following months: \nJanuary,\nFebruary,\nMarch,\nApril,\nMay,\nJune\nAll\n").lower()
        if month in bikesharemonths:
            break
        else:
            print("The month choosen by you is not in the list. Please choose from the list above \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Could you please choose one of the weekdays:\nMonday,\nTuesday,\nWednesday,\nThursday,\nFriday,\nSaturday,\nSunday\nAll\n").lower()
        if day in bikesharedays:
            break
        else:
            print("The weekday choosen by you is not in the list. Please choose from the list above \n")            

    print('-'*40)
    return city, month, day
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print ("Now the data is loading from" + CITY_DATA[city] + ":")
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Manipulating the Start Time information to Date Format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Creating month and day columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Months are filtered (without all)
    if month != 'all':
       	# Creating integers out of month names 
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        # Month Dataframe
        df = df[df['month'] == month]

    # Days are filtered (without all)
    if day != 'all':
        # Day of week dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convertion of the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    # Find the most popular month
    popular_month= df['month'].mode()[0]
    
    # Find the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Popular Start Hour:\n', popular_hour)
    print('Most Popular Start month:\n', popular_month)
    print('Most Popular Start day of week:\n', popular_day_of_week)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The following station is the most commonly used initial station:\n', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('\nThe following station is the most commonly used ending station:\n', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    beginning_ending_stations = df['Start Station'] + "_" + df['End Station']
    trip_counts = beginning_ending_stations.value_counts()
    most_frequent_trip = trip_counts.idxmax()
    print('\nMost frequent used combinations are:\n', most_frequent_trip.split('_')[0], most_frequent_trip.split('_')[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    m, s = divmod(total_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("\nTotal duration of travel: %d days %d hrs %d min %d sec" % (d, h, m, s))

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    m, s = divmod(average_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print('\nAverage duration of travel: %d hrs %d min %d sec' % (h, m, s))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There are ',user_types,' user types')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nThere are ',gender_counts, 'genders')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nEarliest year of birth is ' + str(earliest_birth))
        print('\nMost recent year of birth is ' + str(most_recent_birth))
        print('\nMost common year of birth is ' + str(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs 'yes'. Iterate until user response with a 'no'
    """
    
    count = 0
    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        x = 0
         
    # Check if response is yes, print the raw data and increment count by 5
    if answer.lower() != 'no':
        print(df.iloc[x : x + 5])
        x += 5
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        x = 0
        
    # Otherwise break
    else:
        break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
