import config
import sys
import timeit
import warnings
from data_processing import DataProcessing


def ad_impressions_features_computation(input_file):
    """
    functionality to generate the data frame with only input 'uuid' and new features,
        which would be used create output file.
    :return: output data's data frame
    """
    data = DataProcessing(input_file)       # create the 'DataProcessing' object. 'DataProcessing' is a class with feature extraction and data exploration functionalities implemented.
    print('     DataProcessing object created')
    data.data_visualization()               # data visualization
    return data.feature_extraction()        # feature extraction


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = timeit.default_timer()
    output = ad_impressions_features_computation(sys.argv[1])                      # generate the ad impression's output
    output.to_csv(path_or_buf=sys.argv[2], sep=',', index=False) # write to output file
    elapsed = timeit.default_timer() - start_time
    print('Time (in minutes) taken to generate plots and extract required features and write the output into a file - ' + str(elapsed/60))