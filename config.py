NEW_FIELDS = ['date', 'time', 'weekday']        # new fields generated to use and generate the required features (field used in data_processing.py)
HAND_HELD_DEVICES = ['mobile', 'phone', 'iphone', 'ipad', 'ios', 'tablet', 'tab', 'touch', 'android',
                                  'maemo', 'meego']                                                     # handheld devices predefined set of texts list. (field used in data_processing.py)
DROP_FIELDS = ['hashed_ip', 'ts', 'useragent', 'date', 'time', 'weekday', 'weekday_flag', 'biz_flag']   # fields from data frame to be dropped to produce output. (field used in data_processing.py)
HISTOGRAM_FILE = './plots/Users_Histogram.png'               # User's Histogram based on number of days activity result plot output (field used in data_processing.py)
SCATTER_PLOT_FILE = './plots/Highly_Active_Users_Plot.png'   # graph output to visualize only highly active users (field used in data_processing.py)
