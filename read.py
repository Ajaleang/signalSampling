import pyaudio
import wave

# Abre el archivo de audio
audio_file = wave.open('C:\\Users\\arman\\Documents\\Repositorios\\Down-upSampling\\signal.wav','rb')

# Configura PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(audio_file.getsampwidth()),
                channels=audio_file.getnchannels(),
                rate=audio_file.getframerate(),
                output=True)

# Lee los datos de audio
data = audio_file.readframes(1024)

# Reproduce la señal de audio
while data:
    stream.write(data)
    data = audio_file.readframes(1024)

# Detiene la reproducción
stream.stop_stream()
stream.close()
p.terminate()
