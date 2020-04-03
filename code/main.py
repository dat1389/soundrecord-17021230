import keyboard
import pyaudio
import wave
#https://www.goodreads.com/topic/show/1470148-random-passages-paragraphs
fin = open("para.txt", "rt",encoding='utf8')
fout = open("paraline.txt", "r+",encoding='utf8')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
def record():
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	print("Start recording")
	frames = []
	try:
		while True:
			data = stream.read(CHUNK)
			frames.append(data)
	except KeyboardInterrupt:
		print("Done recording")
		print("#"*80)
		print("\n")
	except Exception as e:
		print(str(e))
	sample_width = p.get_sample_size(FORMAT)
	stream.stop_stream()
	stream.close()
	p.terminate()
	return sample_width, frames	
def record_to_file(file_path):
    wavout=file_path+'_'+str(count)+'.wav'
    wf = wave.open(wavout, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
for line in fin:
	fout.write(line.replace('. ','\n'))

fout.close()

fout = open("paraline.txt", "r+",encoding='utf8')	
a = fout.readlines()
count = len(a)
print("there are "+str(count)+" sentences"+"\n")
def write_line(line_i):
    print(a[line_i])

count = 0
for line in a:
    write_line(count)
    print("press s to start recording")
    while True:
        if keyboard.is_pressed("s"):
            print("recording...")
            print("Press Ctrl+C to stop the recording")
            record_to_file('output')
            break
    count +=1
fin.close()
fout.close()
print('done')