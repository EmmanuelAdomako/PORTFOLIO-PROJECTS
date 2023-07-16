#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import datetime


# In[2]:


#Load or Read the data
data = df =pd.read_csv(r"C:\Users\USER\Desktop\Capstone_Project\202305-divvy-tripdata.csv")


# In[3]:


data.head(2)


# In[4]:


#Rename the columns 

data = data.rename(columns={
    'ride_id': 'trip_id',
    'rideable_type': 'bikeid',
    'started_at': 'start_time',
    'ended_at': 'end_time',
    'start_station_name': 'from_station_name',
    'start_station_id': 'from_station_id',
    'end_station_name': 'to_station_name',
    'end_station_id': 'to_station_id',
    'member_casual': 'usertype'
})


# In[14]:


#summary of data
data.head(10)


# In[11]:


print(data.info())


# In[15]:


data.describe()


# In[18]:


df.duplicated().sum()


# In[21]:


df.isnull().any().sum()


# In[22]:


data = data.replace("", np.nan)  # Replace empty strings with NaN
data = data.fillna("Null")  # Replace NaN with "Null"


# In[24]:


data


# In[29]:


# Convert 'ended_at' and 'started_at' columns to datetime format
data['end_time'] = pd.to_datetime(data['end_time'])
data['start_time'] = pd.to_datetime(data['start_time'])


# In[30]:


data.dtypes


# In[31]:


#Creat a Column "Ride_length" by subtracting "ended_at" from "started_at"
data['ride_length'] = data['end_time'] - data['start_time']


# In[32]:


data


# In[34]:


#Convert ride length to seconds
data['ride_length'] = (data['end_time'] - data['start_time']).dt.total_seconds()


# In[35]:


data


# In[36]:


data.dtypes


# In[37]:


#check for negative ride_length entries (Bad data)
negative_entries = data[data['ride_length'] < 0]['ride_length']
print(negative_entries)


# In[38]:


#Removing the bad data 
data = data[data['ride_length'] >= 0]


# In[41]:


data


# In[46]:


#check if "usertype" column contains only "subscriber" and "customer" entries
subscriber_entries = data[data['usertype'] == 'Subscriber']
customer_entries = data[data['usertype'] == 'Customer']

print(subscriber_entries)
print(customer_entries)


# In[48]:


#check for unique entries
unique_user_types = data['usertype'].unique()
print(unique_user_types)


# In[49]:


#descriptive analysis(in seconds)
mean_ride_length = data['ride_length'].mean()
median_ride_length = data['ride_length'].median()
max_ride_length = data['ride_length'].max()
min_ride_length = data['ride_length'].min()

print("Mean ride length:", mean_ride_length)
print("Median ride length:", median_ride_length)
print("Maximum ride length:", max_ride_length)
print("Minimum ride length:", min_ride_length)


# In[53]:


#Compare members and casual users

mean_ride_length = data.groupby('usertype')['ride_length'].mean()
median_ride_length = data.groupby('usertype')['ride_length'].median()
max_ride_length = data.groupby('usertype')['ride_length'].max()
min_ride_length = data.groupby('usertype')['ride_length'].min()

print("Mean ride length by user type:")
print(mean_ride_length)
print("\nMedian ride length by user type:")
print(median_ride_length)
print("\nMaximum ride length by user type:")
print(max_ride_length)
print("\nMinimum ride length by user type:")
print(min_ride_length)



# In[54]:


data.head(2)


# In[65]:


df.loc['start_time'] = pd.to_datetime(data['start_time'])
df.loc['day_of_week'] = data['start_time'].dt.weekday + 1


# In[67]:


data


# In[68]:


data.isnull().any().sum()


# In[69]:


data = data.replace("", np.nan)  # Replace empty strings with NaN
data = data.fillna("Null")  # Replace NaN with "Null"


# In[70]:


data.isnull().any().sum()


# In[71]:


data


# In[75]:


# Remove rows with missing or invalid ride_length values
data = data[data['ride_length'].notna()]

# Convert ride_length to numeric
data['ride_length'] = pd.to_numeric(data['ride_length'], errors='coerce')

# Calculate the average ride time by each day for members vs casual users
average_ride_time = data.groupby(['usertype', 'day_of_week'])['ride_length'].mean()
print(average_ride_time)


# In[91]:


# Calculate the average ride length by day of the week for members and casual users
weekly_average_ride_length = data.groupby(['day_of_week', 'usertype'])['ride_length'].mean().reset_index()
weekly_average_ride_length_df = pd.DataFrame(weekly_average_ride_length)

# Set the order of days of the week
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Create separate DataFrames for members and casual users
members_df = weekly_average_ride_length_df[weekly_average_ride_length_df['usertype'] == 'member']
casual_df = weekly_average_ride_length_df[weekly_average_ride_length_df['usertype'] == 'casual']

# Plotting the bar chart
pos = list(range(len(days_of_week)))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
plt.bar(pos, members_df['ride_length'], width, alpha=0.5, color='b', label='Members')
plt.bar([p + width for p in pos], casual_df['ride_length'], width, alpha=0.5, color='r', label='Casual Users')

# Adding labels and titles
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(days_of_week)
plt.xlabel('Day of the Week')
plt.ylabel('Average Ride Length')
plt.title('Average Ride Length for Riders by Day of the Week')
plt.legend(['Members', 'Casual Users'])

# Display the chart
plt.show()


# In[215]:


data.head(2)


# In[ ]:





# In[216]:


total_ride_count = data['trip_id'].count()
print("Total ride count:", total_ride_count)


# In[218]:


ride_count_by_user_type = data.groupby('usertype')['trip_id'].count()
print(ride_count_by_user_type)


# In[225]:


ride_count_by_user_type = data.groupby('usertype')['trip_id'].count()
total_ride_count = ride_count_by_user_type.sum()
ride_percentage_by_user_type = (ride_count_by_user_type / total_ride_count) * 100
print(ride_percentage_by_user_type)



# In[102]:


# Filter out null entries
filtered_data = data[data['usertype'].notnull()]

# Calculate the count of each rider category
ride_counts = filtered_data['usertype'].value_counts()

# Remove the null category from the count
ride_counts = ride_counts.dropna()

# Plot the pie chart
plt.pie(ride_counts, labels=ride_counts.index, autopct='%1.1f%%')
plt.title('Ride Distribution by Rider Category')
plt.axis('equal')
plt.show()


# In[135]:


total_bike_hires = data.groupby('usertype')['bikeid'].count()

# Print the total bike hires among users
print(total_bike_hires)

# Define the colors for the bar chart
colors = ['pink', 'yellow']

# Create a bar chart
plt.bar(total_bike_hires.index, total_bike_hires.values, color=colors)

# Set the y-axis label
plt.ylabel('Total Bike Hires')

# Set the chart's title
plt.title('Total Bike Hires Among Users')

# Show the plot
plt.show()


# In[136]:


# Group the data by user type and calculate the mean of the ride length
average_ride_length = data.groupby('usertype')['ride_length'].mean()

# Print the average ride length
print(average_ride_length)


# Calculate the average ride length between user types
average_ride_length = data.groupby('usertype')['ride_length'].mean().sort_values()

# Assign colors based on the average ride length ranking
colors = ['red' if user == average_ride_length.idxmin() else 'green' if user == average_ride_length.idxmax() else 'skyblue' for user in average_ride_length.index]

# Create a bar chart
plt.bar(average_ride_length.index, average_ride_length.values, color=colors)

# Set the y-axis label
plt.ylabel('Average Ride Length')

# Set the chart title
plt.title('Average Ride Length between User Types')

# Show the plot
plt.show()


# In[140]:


#compare the bike hires and ride length among usertypes 

# Group the data by user type and calculate the sum of the ride length and the count of bike hires
ride_length_sum = data.groupby('usertype')['ride_length'].sum()
bike_hires_count = data.groupby('usertype')['bikeid'].count()

# Print the ride length and bike hires
print("Ride Length:")
print(ride_length_sum)
print("\nBike Hires:")
print(bike_hires_count)

# Create a colormap ranging from red to green
colormap = plt.cm.RdYlGn(np.linspace(0, 1, len(ride_length_sum)))

# Create a bar chart for ride length with color mapping
plt.subplot(1, 2, 1)
ride_length_sum.plot(kind='bar', color=colormap)
plt.ylabel('Total Ride Length')
plt.title('Ride Length Among Users')

# Create a bar chart for bike hires with color mapping
plt.subplot(1, 2, 2)
bike_hires_count.plot(kind='bar', color=colormap)
plt.ylabel('Total Bike Hires')
plt.title('Bike Hires Among Users')

# Adjust the layout and spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()


# In[141]:


#Determining the unique bike_types 

unique_bike_ids = data['bikeid'].unique()
print(unique_bike_ids)


# In[142]:


user_bikes = data.groupby('usertype')['bikeid'].unique()
print(user_bikes)


# In[162]:


# Group the data by usertype and bike type, and calculate the count of rides
bike_type_counts = data.groupby(['usertype', 'bikeid'])['bikeid'].count()

# Convert the resulting series to a dataframe
bike_type_counts_df = bike_type_counts.unstack()

# Print the dataframe
print(bike_type_counts_df)


# Group the data by bike type and user type, and calculate the count of rides
bike_type_counts = data.groupby(['bikeid', 'usertype']).size().unstack()

# Get the bike types and user types
bike_types = bike_type_counts.index
user_types = bike_type_counts.columns

# Define the colors for each bike type
colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']

# Create an array of indices for the x-axis ticks
x_ticks = np.arange(len(bike_types))

# Create the grouped bar chart
fig, ax = plt.subplots()
width = 0.35

for i, user_type in enumerate(user_types):
    counts = bike_type_counts[user_type].values
    ax.bar(x_ticks + i * width, counts, width, label=user_type, color=colors[i])

# Set the x-axis tick labels to the bike types
ax.set_xticks(x_ticks)
ax.set_xticklabels(bike_types)

# Set the y-axis label
ax.set_ylabel('Number of Rides')

# Set the chart title and legend
ax.set_title('Bike Types Ridden by Members and Casual Users')
ax.legend()

# Display the chart
plt.show()


# In[172]:


#Determine the day with highest bike hires

# Convert 'start_time' column to datetime format if it's not already
data['start_time'] = pd.to_datetime(data['start_time'])

# Extract the day of the week from the 'start_time' column
data['day_of_week'] = data['start_time'].dt.day_name()

# Group the data by day of the week and calculate the count of bike hires
daily_bike_hires = data.groupby('day_of_week')['bikeid'].count()

# Find the day(s) with the highest bike hires
highest_hires_days = daily_bike_hires[daily_bike_hires == daily_bike_hires.max()]

# Print the result
for day, hires in highest_hires_days.items():
    print(f"The day with the highest bike hires is {day} with {hires} hires.")


# In[173]:


# Convert 'start_time' column to datetime format if it's not already
data['start_time'] = pd.to_datetime(data['start_time'])

# Extract the day of the week from the 'start_time' column and format it
data['day_of_week'] = data['start_time'].dt.day_name().str.title()

# Group the data by day of the week and calculate the count of bike hires
daily_bike_hires = data.groupby('day_of_week')['bikeid'].count()

# Find the day(s) with the highest bike hires
max_hires = daily_bike_hires.max()
days_with_max_hires = daily_bike_hires[daily_bike_hires == max_hires].index

# Print the days with the highest bike hires
print("Days with the highest bike hires:")
print(days_with_max_hires)

# Create a bar chart of bike hires by day of the week
plt.bar(daily_bike_hires.index, daily_bike_hires.values)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Bike Hires')
plt.title('Bike Hires by Day of the Week')

# Highlight the days with the highest bike hires in a different color
for day in days_with_max_hires:
    plt.gca().get_xticklabels()[daily_bike_hires.index.get_loc(day)].set_color('red')

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# In[176]:



# Group the data by day of the week and calculate the count of bike rides
daily_bike_rides = data.groupby('day_of_week')['bikeid'].count()

# Find the day with the lowest bike rides
min_rides = daily_bike_rides.min()
day_with_min_rides = daily_bike_rides[daily_bike_rides == min_rides].index[0]

# Print the day with the lowest bike rides
print("Day with the lowest bike rides:")
print(day_with_min_rides)


# In[177]:


data.head(2)


# In[181]:


stations_available = data.groupby('from_station_name')['from_station_name'].unique()
print(stations_available)


# In[ ]:





# In[184]:


# Calculate the average ride length for users by day of the week
average_ride_length = data.groupby('day_of_week')['ride_length'].mean()

# Plot the average ride length
plt.figure(figsize=(8, 5))
plt.plot(average_ride_length.index, average_ride_length.values, marker='o')
plt.xlabel('Day of the Week')
plt.ylabel('Average Ride Length')
plt.title('Average Ride Length for Users by Day of the Week')
plt.xticks(rotation=45)
plt.show()


# In[192]:


# Group the data by 'bike_type' and count the occurrences
most_ridden_bike_type = data['bikeid'].value_counts().idxmax()

# Print the most ridden bike type
print("Most ridden bike type:", most_ridden_bike_type)


# In[193]:


# Group the data by 'bike_type' and count the occurrences
bike_type_counts = data['bikeid'].value_counts()

# Plot a bar chart of bike type counts
plt.bar(bike_type_counts.index, bike_type_counts.values)
plt.xlabel('Bike Type')
plt.ylabel('Count')
plt.title('Most Ridden Bike Type')

# Show the plot
plt.show()

