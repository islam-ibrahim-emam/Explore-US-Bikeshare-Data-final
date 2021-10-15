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

    cities=['chicago', 'new york city', 'washington']
    data_valid = 0
    while data_valid == 0:
        city = input("Pleas chose a city (chicago, new york city, washington) \n").lower()
        if (city in cities ):
            data_valid = 1
        else:
            print("worng city input")
            continue

        # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    data_valid = 0
    while data_valid == 0:
        month = input("Pleas enter a month as string or all to get all data:\n").lower()
        if (month in months):
            data_valid=1
        else:
            print("worng month input")
            continue


#Sunday Monday Tuesday - Wednesday ! Thursday ! Friday , Saturday
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    data_valid = 0
    while data_valid == 0:
        day = input("Please enter filter day or all to get all data: \n").lower()
        if (day in days):
            data_valid = 1

        else:
            print("worng day input")
            continue

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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['Start hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]    # mask from data analysis classes

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def display_data(city):
    """
    this function take data frame as input and show it to the user to imagin how it looks like
    """

    df = pd.read_csv(CITY_DATA[city])
    print('\n Do you want to see the first 5 rows of data? \n')
    start_indx = 0
    while True:
        user_display = input('To View the first 5 rows of data type: Yes if you dont want type no \n').lower()
        if user_display not in ['yes', 'no']:
            print('That\'s invalid data input pleas Enter (yes or no)')
        elif user_display == 'yes':
            print(df.iloc[start_indx:start_indx+5, : ])
            start_indx += 5
        elif user_display == 'no':
            print('\n no display data is needed...')
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month:", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour:", df['Start hour'].mode()[0])


    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station :", df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("Most commonly used end station :", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station :", df.groupby(['Start Station','End Station']).size().sum())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time :", df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print("Mean travel time :", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\n Calculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print('Counts of gender:')
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')

        most_common_year = df['Birth Year'].mode()[0]
        print('most common year:',most_common_year)

        most_recent_year = df['Birth Year'].max()
        print('most recent year:',most_recent_year)

        earliest_year = df['Birth Year'].min()
        print('earliest year:',earliest_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
