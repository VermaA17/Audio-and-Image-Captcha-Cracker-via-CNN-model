import os
import numpy as np
import matplotlib.pylab as plt
from os import listdir
from os.path import isfile,join
import os
#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
#import IPython.display as ipd
path="C:/captcha-demo-master/pr3_data"
dest = "C:/captcha-demo-master/pr3_aud_s"
files = [f for f in listdir(path) if isfile(join(path,f))]
#gray= file.open(self.directory_name + "/" + random_image_file)
#audio_clips = os.listdir(audio_fpath)
#x, sr = librosa.load('C:/Users/spanda/Desktop/Trinity/projects/scalable/project3/test/00c1e4c84471076968f46eeca30cd9069d369d71.mp3', sr=44100)
count = 0
for audio in files:
    x, sr = librosa.load(os.path.join(path, audio))
    plt.figure(figsize=(1.28, .64), dpi=100)
    plt.axis('off')
    plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
    S = librosa.feature.melspectrogram(y=x, sr=sr)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    plt.savefig(os.path.join(dest, os.path.splitext(audio)[0]+'.png'), bbox_inches=None, pad_inches=0)
    count = count+1
    print(count)
    plt.close()