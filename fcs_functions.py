"""
File containing all necessary functions to work with FCS files (For both compensated and uncompensated files).

Functions:

create_graph(filePath: str, channels: {channelOne: str, channelTwo: str}, mode: str, colorbar: bool) -> {graphPath: str, errorCode: int}

Creates a density2d graph of the provided fcs file, will then return an obj. with the path to the graph and an error code.
"""
import FlowCal
import matplotlib.pyplot as plt
import os


def create_graph(file_path: str, output_dir: str, file_name: str,
                 channels: dict = {'channel_one': 'SSC56-A', 'channel_two': 'FSC58-A'},
                 mode: str = 'scatter', colorbar: bool = True) -> dict:
    try:
        s = FlowCal.io.FCSData(file_path)  # Load the FCS file into a FlowCal FCSData object

        # creating the density plot
        FlowCal.plot.density2d(s, channels=[channels['channel_one'], channels['channel_two']], mode=mode, colorbar=True)

        output_path = os.path.join(output_dir, f'{file_name}.png')
        plt.savefig(output_path)

        # Clear the plot to prevent overlapping plots in future calls
        plt.clf()
        return {"graphPath": "", "errorCode": -1}
    except Exception as e:
        print(e)
        return {"graphPath": "", "errorCode": -1}