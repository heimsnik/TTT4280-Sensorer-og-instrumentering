import numpy as np
import matplotlib.pyplot as plt

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        # Read the sample period from the file
        sample_period_us = np.fromfile(file, dtype=np.float64, count=1)[0]

        # Read the ADC data from the file
        adc_data = np.fromfile(file, dtype=np.uint16)

    return sample_period_us, adc_data

def plot_adc_data(sample_period_us, adc_data, num_samples, num_channels):
    time_axis = np.arange(0, num_samples * sample_period_us * 1e-6, sample_period_us * 1e-6)

    plt.figure(figsize=(12, 6))
    for i in range(num_channels):
        plt.plot(time_axis, adc_data[i::num_channels], label=f'Channel {i + 1}')

    plt.title('ADC Data')
    plt.xlabel('Time (seconds)')
    plt.ylabel('ADC Value')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Path to the binary file generated by the C program
    binary_file_path = "../Data/sampled_data_22-24-27.bin"

    # Number of samples and channels (adjust according to your setup)
    num_samples = 31250  # Update with the actual number of samples
    num_channels = 5     # Update with the actual number of ADC channels

    # Read data from the binary file
    sample_period_us, adc_data = read_binary_file(binary_file_path)

    # Plot the ADC data
    plot_adc_data(sample_period_us, adc_data, num_samples, num_channels)