from matplotlib.pyplot import show, colorbar
from ltsa import WavLTSA
import glob, os

# generates LTSAs for all .wav files in a specified directory
dir = '/Users/josh/OWL/Data/ACTIVE_WAVS'
# some reasonable settings for a 44.1kHz sampling rate
params = {'div_len': 22050,
          'subdiv_len': 4096,
          'nfft': 4096,
          'noverlap': 1000}

for file in os.listdir(dir):
    if file.endswith(".wav"):
        fn = os.path.join(dir, file)
        outfn = fn[:-4] + "_LTSA.pdf"
        print "Processing file:", fn

        # initialize the object with raw data from wav file
        s = WavLTSA(fn)

        # apply the parameters
        s.set_params(params)

        # compute the LTSA -- identical to s.compute()
        s()

        # throw out data over 6kHz as there isn't much interesting activity there
        # in a typical song
        s.crop(fmax=6000)

        # save and show
        s.save(outfn, 600)
        print "Output LTSA:", outfn
        # s.show()
