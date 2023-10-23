import sys
import librosa.display 
import matplotlib.pyplot as plt

args = sys.argv
filename = str(args[1])

y,sr = librosa.load("./wav/" + filename + ".wav")
rms=librosa.feature.rms(y=y) #RMSを計算

# dBの基準値となる値は騒音計と同様である2*1e-5を使用
db=librosa.amplitude_to_db(rms,ref=2*1e-5) #dBを計算
time=librosa.times_like(db,sr=sr) #時間軸の生成

# グラフをプロットして保存
plt.xlabel("Time(s)")
plt.ylabel("dB")
plt.plot(time,db[0])
plt.savefig("./result/" + filename + ".jpg")