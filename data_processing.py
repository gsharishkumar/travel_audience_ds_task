import config
import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot


class DataProcessing:

    def __init__(self, input_file):
        print('Fetching data from input file and creating the DataProcessing Object...')
        # read input data file
        self.data_df = pd.read_csv(input_file, sep=',')                   # input data into data frame
        # create new fields date, time, and weekday from input data
        self.data_date = pd.to_datetime(self.data_df['ts']).dt.date             # date from ts field data
        self.data_time = pd.to_datetime(self.data_df['ts']).dt.time             # time from ts field data
        self.data_weekday = pd.to_datetime(self.data_df['ts']).dt.weekday       # week day number from ts field data
        # create data frame to have new fields date, time, and weekday
        data_new_df = pd.DataFrame()
        new_fields = [self.data_date, self.data_time, self.data_weekday]
        data_new_df = pd.concat(new_fields, axis=1)                 # new data frame with newly created fields
        data_new_df.columns = config.NEW_FIELDS                                 # newly created fields column names
        # concatinate the newly created data frame 'data_new_df' with the data frame 'self.data_df' created from input file
        frames = [self.data_df, data_new_df]
        self.data_df = pd.concat(frames, axis=1)                                # concatinated data frame

    def feature_extraction(self):
        """
        Functionality to extract new features 'highly_active', 'multiple_days',
        'weekday_biz', and 'device_type' from input data.
        :param data: chuck of input data records
        :return: data frame, with chuck of input data records with output features
        """
        print('Extracting features...')
        grouped_data_df = self.data_df['date'].groupby(self.data_df['uuid'])
        self.highly_active_extraction(grouped_data_df)
        print('     Extracted highly_active feature')
        self.multiple_days_extraction(grouped_data_df)
        print('     Extracted multiple_days feature')
        self.weekday_biz_extraction()
        print('     Extracted weekday_biz feature')
        self.device_type_extraction()
        print('     Extracted device_type feature')
        self.data_df = self.data_df.drop(config.DROP_FIELDS, axis=1)  # drop the input fields except 'uuid'
        return self.data_df

    def highly_active_extraction(self, grouped_data):
        """
        functionality to extract 'highly_active' feature values from input data and update the new feature 'highly_active' in the dataframe.
        highly_active rule followed:
            if the user is active on 15 or more days of months then considered highly active (true) else not highly active (false).
        :param grouped_data: grouped date data on uuid from input data
        :return: None
        """
        self.data_df['highly_active'] = grouped_data.transform(lambda x: x.nunique() >= 15)

    def multiple_days_extraction(self, grouped_data):
        """
        functionality to extract 'multiple_days' feature from input data and update the new feature 'multiple_days' in the dataframe.
        multiple_days rule followed:
            if the user is active on more than 1 day then considered active on multiple days (True) else not active on multiple days (False).
        :param grouped_data: grouped date data on uuid from input data
        :return: None
        """
        self.data_df['multiple_days'] = grouped_data.transform(lambda x: x.nunique() > 1)

    def weekday_biz_extraction(self):
        """
        functionality to extract 'weekday_biz' feature from input data and update the new feature 'weekday_biz' in the dataframe.
        weekday_biz rule followed:
            if the user is active on week day during business hours then considered True else False.
            Week days: Monday(0), Tuesday(1), Wednesday(2), Thursday(3), Friday(4)
            Business hours: 08:00 to 18:00
        :return: None
        """
        biz_from_time = datetime.time(8, 00)  # biz hours start time
        biz_to_time = datetime.time(18, 00)  # biz hours end end
        self.data_df['weekday_flag'] = self.data_df['weekday'].groupby(self.data_df['uuid']).transform(
            lambda x: x <= 4)
        self.data_df['biz_flag'] = self.data_df['time'].apply(lambda x: (biz_from_time <= x) & (x <= biz_to_time))
        self.data_df['weekday_biz'] = self.data_df['weekday_flag'] & self.data_df['biz_flag']

    def device_type_extraction(self):
        """
        functionality to extract 'device_type' feature values from input data and update the new feature 'device_type' in the dataframe.
        device_type rule followed:
            based on the useragent string, the user's device type is decided.
            Only three devices are considered namely 'hand held devices', 'smart television', and 'other devices(computers, pc...)'
            Predefined text occurrence in input 'useragent' match is the logic used to find the device type.
            'hand held devices' predefined text to find in 'useragent': 'mobile', 'phone', 'iphone', 'ipad', 'ios', 'tablet', 'touch' (to find touch devices),
                'maemo' (Nokia Linux mobile), 'meego' (Nokia Linux mobile)
            'smart television' predefined text to find in 'useragent': 'tv'
            'other devices': if the above predefined texts not available in useragent.
        Feature values: 1 for 'hand held devices', 2 for 'smart television', 3 for 'other devices'
        :return: None
        """
        handheld_devices_texts = config.HAND_HELD_DEVICES  # handheld devices predefined set of texts list
        self.data_df['device_type'] = self.data_df['useragent'].apply(lambda x: 3 if type(x) is not str else (
            1 if any(text in x.lower() for text in handheld_devices_texts) else (2 if 'tv' in x.lower() else 3)))

    def data_visualization(self):
        """
        Functionality to prepare required data and plot graphs to visualize highly active users and
        each user's number of days activity.
        :return: None
        """
        print('Data visualization...')
        # to find each user's number of days activity
        users_active_unique_date_counts = self.data_df['date'].groupby(self.data_df['uuid']).nunique()

        # plot configuration
        fig1 = pyplot.figure()
        ax1 = fig1.add_subplot(3, 1, 1)
        ax2 = fig1.add_subplot(3, 1, 2)
        ax3 = fig1.add_subplot(3, 1, 3)
        fig1.suptitle("User's Histogram based on number of days activity")

        #User's Histogram based on number of days activity - numbers of active days counts considered are 1, 2, 3
        ax1.hist(users_active_unique_date_counts, bins=[0, 1, 2, 3])
        ax1.margins(0.1)
        xlabels = [0, 1, 2, 3]
        ax1.set_xticks(np.arange(len(xlabels)))
        ax1.set_xticklabels(xlabels)

        # User's Histogram based on number of days activity - numbers of active days counts considered in buckets namely (3 to 5, 6 to 8, 9 to 11, 12 to 14)
        ax2.hist(users_active_unique_date_counts, bins=[3, 6, 9, 12, 15])
        ax2.margins(0.1)
        xlabels1 = [0, 3, 6, 9, 12, 15]
        ax2.set_xticks(3 * np.arange(len(xlabels1)))
        ax2.set_xticklabels(xlabels1)
        ax2.set_ylabel('Number of unique users')

        # User's Histogram based on number of days activity - numbers of active days counts considered in buckets namely (11 to 14, 15 to 19, 20 to 24, 25 to 31)
        ax3.hist(users_active_unique_date_counts, bins=[10, 15, 20, 25, 32])
        ax3.margins(0.1)
        xlabels3 = [0, 5, 10, 15, 20, 25, 32]
        ax3.set_xticks(5 * np.arange(len(xlabels3)))
        ax3.set_xticklabels(xlabels3)
        ax3.set_xlabel('Number of days user active')

        fig1.savefig(config.HISTOGRAM_FILE)
        # rest of the code - to create a plot to visualize highly active users impressions count on each day

        # create a dataframe with unique users and their's active days count (columns: users, user_impressions_unique_days_count)
        user_days_count_df = pd.DataFrame({'user_impressions_unique_days_count': self.data_df['date'].groupby(
            self.data_df['uuid']).nunique()}).reset_index()
        # create a dataframe with impression count for each user and date combination (columns: users, date, user_impression_count)
        user_impression_count_df = pd.DataFrame( self.data_df.groupby(['uuid', 'date']).size()).reset_index()
        # unstack the user_impression_count_df to create dates index and multiple uuid's columns,
        # each having impression counts on the index date for the column named uuid user
        impression_count_df = pd.DataFrame(user_impression_count_df.set_index(["uuid", "date"]).unstack(level=0))
        impression_count_df = impression_count_df.replace(np.nan, 0)    # replace nan with 0 (ie., no impression on that date)
        # structure the impression_count_df to easily plot as required
        new_column_names = [value[1] for value in impression_count_df.columns.values]
        impression_count_df.columns = new_column_names
        # fetch only highly active users records
        highly_active_users = list(user_days_count_df[user_days_count_df['user_impressions_unique_days_count'] >= 15]['uuid'])
        highly_active_users_df = impression_count_df.loc[:, highly_active_users]
        print('     Number of highly active users - '+ str(len(highly_active_users_df.columns)))
        # other users records - not used for plot
        other_users_df = impression_count_df.drop(highly_active_users, axis=1)
        print('     Other users count -- ' + str(len(other_users_df.columns)))
        # plot the graph to visualize only highly active users
        # highly_active_users_df dataframe contains highly active user ips as the columns and indices as dates,
        # and the values in each columns are the impression counts
        ax = highly_active_users_df.plot(marker='o',  title='Visualization of only highly active users', legend=False)
        ax.set_xlabel('July 2017 Dates')
        ax.set_ylabel('Each User\'s impression counts')
        fig2 = ax.get_figure()
        fig2.savefig(config.SCATTER_PLOT_FILE)
        print('     Plots are generated in ./plots folder')