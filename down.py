import wave
import numpy as np
import scipy.signal

# Abre el archivo de audio original
audio_file = wave.open('C:\\Users\\arman\\Documents\\Repositorios\\Down-upSampling\\signal.wav', 'rb')

# Lee los parámetros del archivo de audio
nchannels = audio_file.getnchannels()
sampwidth = audio_file.getsampwidth()
framerate = audio_file.getframerate()
nframes = audio_file.getnframes()

# Lee los datos de audio y los convierte a un array NumPy
audio_data = audio_file.readframes(nframes)
audio_data = np.frombuffer(audio_data, dtype=np.int16)

# Downsampling de la señal de audio
downsampling_factor = 2
audio_data_downsampled = scipy.signal.decimate(audio_data, downsampling_factor)

# Crea un nuevo archivo para guardar la señal de audio downsampling
audio_file_downsampled = wave.open('audio_downsampled.wav', 'wb')

# Configura los parámetros del archivo de audio downsampling
audio_file_downsampled.setnchannels(nchannels)
audio_file_downsampled.setsampwidth(sampwidth)
audio_file_downsampled.setframerate(framerate/downsampling_factor)

# Escribe los datos de audio downsampling en el archivo
audio_file_downsampled.writeframes(audio_data_downsampled.tobytes())

# Cierra los archivos de audio
audio_file.close()
audio_file_downsampled.close()
