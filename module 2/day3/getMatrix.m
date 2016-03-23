[x,fs]=audioread('english_horn.wav')
y=linspace(0,length(x)/fs,length(x))
y=transpose(y)
