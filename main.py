#!/usr/bin/env/python3

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

import mne

sample_data_folder = Path("pycrostates_2-20/data")

print(sample_data_folder)
sample_data_raw_file = sample_data_folder / "sub-010002_EC_avgref_1-30Hz_ep00_raw.fif"
# sample_data_raw_file = sample_data_folder / "MEG" / "sample" / "sample_audvis_raw.fif"
# raw = mne.io.read_raw_fif(sample_data_raw_file)
# raw.crop(tmax=60).load_data()

x = mne.io.read_raw(sample_data_folder / "sub-010002_EC_avgref_1-30Hz_ep00_raw.fif")
data = x.get_data()

x.plot(
    n_channels=32,      # number of channels displayed
    scalings='auto',
    duration=10         # seconds shown at once
)
plt.show()

# 