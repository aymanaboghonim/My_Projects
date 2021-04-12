import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("""\n Please choose your city from the following :
              \n 1. Chicago
              \n 2. New York City
              \n 3. Washington""")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\n You entered Invalid name !please, retry again!  ")
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_LIST = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_LIST.keys():
        print("\n Please enter a valid month name between January to June or enter All to view all months")
        month = input().lower()

        if month not in MONTH_LIST.keys():
            print("\nYou entered Invalid name !please, retry again!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['saturday', 'sunday' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all' ]
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a valid day name  or enter All to view all days")
        day = input().lower()

    print('_'*30)
    return city, month, day

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    The_Most_Popular_Start_Station  = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {The_Most_Popular_Start_Station}")

    # TO DO: display most commonly used end station
    The_Most_Popular_End_Station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {The_Most_Popular_End_Station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['start station & end station'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_frequent_combination= df['start station & end station'].mode()[0]

    print(f"\nmost frequent combination of start station and end station trip is {most_frequent_combination}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time  = round(df['Trip Duration'].mean())
    print(f"The mean travel time is {mean_travel_time}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"The count of user types is : {user_types}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
        gender_count = df['Gender'].value_counts()
        print(f"\nThe count of gender is : {gender_count}")
    else:
        print('No gender data in this City!')    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest_year_of_birth= int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        common_year_of_birth = int(df['Birth Year'].mode()[0])
        print(f"""\nThe earliest year of birth: {earliest_year_of_birth}\n
             \nThe most recent year of birth:{most_recent_year_of_birth}\n
            \nThe most common year of birth: {common_year_of_birth}""")
    else:
        print('No Birth data in this City! ')        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    def display_raw_data(df):
        '''
        This function displays five rows of raw data upon request by the user 
    I
    
    '''
    
    counter = 0

    five_rows = input("\n Would you like to see five rows of raw data ? Please write 'yes' if you want to proceed or 'no' to skip  \n").lower()
    while True:
        if five_rows == 'no':
            print("bye bye!")
            break
        if five_rows == 'yes':
            print(df[counter: counter + 5])
            counter = counter + 5
        five_rows = input("\n Would you like to see another five rows ? Please write 'yes' to proceed or 'no'  to skip \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Bye Bye !")
            break


if __name__ == "__main__":
	main()
