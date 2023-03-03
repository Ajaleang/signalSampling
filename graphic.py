import wave
import numpy as np
import matplotlib.pyplot as plt

# Abre el archivo de audio
audio_file = wave.open('C:\\Users\\arman\\Documents\\Repositorios\\Down-upSampling\\signal.wav', 'rb')

# Lee los parámetros del archivo de audio
nchannels = audio_file.getnchannels()
sampwidth = audio_file.getsampwidth()
framerate = audio_file.getframerate()
nframes = audio_file.getnframes()
audio_data = audio_file.readframes(nframes)
# Calcula el tiempo en segundos de cada muestra
time = np.arange(0, nframes) / framerate
time = time[:len(audio_data)]

# Lee los datos de audio y los convierte a un array NumPy

audio_data = np.frombuffer(audio_data, dtype=np.int16)[:len(time)]


# Grafica la magnitud vs tiempo de la señal de audio
plt.plot(time, audio_data)
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Magnitud')
plt.show()

# Cierra el archivo de audio
audio_file.close()
