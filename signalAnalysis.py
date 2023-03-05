import wave
import numpy as np
import matplotlib.pyplot as plt

# Abrir archivo de audio en formato WAV
archivo_audio = wave.open('C:\\Users\\arman\\Documents\\Repositorios\\Down-upSampling\\signal.wav', 'r')

# Obtener los parámetros del archivo de audio
num_canales = archivo_audio.getnchannels()
frec_muestreo = archivo_audio.getframerate()
num_frames = archivo_audio.getnframes()

# Leer los datos de audio en un array de numpy
datos_audio = archivo_audio.readframes(num_frames)
datos_audio = np.frombuffer(datos_audio, dtype=np.int16)

# Cerrar el archivo de audio
archivo_audio.close()

# Generar la gráfica de la señal de audio
plt.plot(datos_audio)
plt.title('Señal de audio original')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud')
plt.show()

# Upsampling de la señal de audio
upsampled_audio = np.zeros(len(datos_audio)*10)
upsampled_audio[::10] = datos_audio

# Crear archivo de audio upsampled en formato WAV
archivo_audio_upsampled = wave.open('audio_upsampled.wav', 'w')
archivo_audio_upsampled.setnchannels(num_canales)
archivo_audio_upsampled.setframerate(frec_muestreo*2)
archivo_audio_upsampled.setsampwidth(archivo_audio.getsampwidth())

# Escribir los datos de audio upsampled en el archivo WAV
archivo_audio_upsampled.writeframes(upsampled_audio.astype(np.int16).tobytes())

# Cerrar el archivo de audio upsampled
archivo_audio_upsampled.close()

# Reproducir la señal de audio upsampled
plt.plot(upsampled_audio)
plt.title('Señal de audio upsampled')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud')
plt.show()

# Downsampling de la señal de audio
downsampled_audio = datos_audio[::10]

# Crear archivo de audio downsampled en formato WAV
archivo_audio_downsampled = wave.open('audio_downsampled.wav', 'w')
archivo_audio_downsampled.setnchannels(num_canales)
archivo_audio_downsampled.setframerate(frec_muestreo//10)
archivo_audio_downsampled.setsampwidth(archivo_audio.getsampwidth())

# Escribir los datos de audio downsampled en el archivo WAV
archivo_audio_downsampled.writeframes(downsampled_audio.astype(np.int16).tobytes())

# Cerrar el archivo de audio downsampled
archivo_audio_downsampled.close()

# Reproducir la señal de audio downsampled
plt.plot(downsampled_audio)
plt.title('Señal de audio downsampled')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud')
plt.show()
