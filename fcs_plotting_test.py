import FlowCal
import FlowCal.transform
import numpy as np
import matplotlib.pyplot as plt


s = FlowCal.io.FCSData('FCS_Files/Compensated_Files/CD274 BV 785 Run 1 20231010143028.fcs')

print(s.shape)
print(s.channels)

FlowCal.plot.density2d(s, channels=['FSC58-A', 'SSC56-A'], mode='scatter', colorbar=True)
plt.show()
