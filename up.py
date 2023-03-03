import wave

# Abre el archivo de audio original
audio_file = wave.open('C:\\Users\\arman\\Documents\\Repositorios\\Down-upSampling\\signal.wav', 'rb')

# Obtiene los parámetros del archivo original
nchannels, sampwidth, framerate, nframes, comptype, compname = audio_file.getparams()

# Define el factor de upsampling
upsampling_factor = 2

# Crea un nuevo archivo de audio con el doble de la frecuencia de muestreo
audio_upsampled = wave.open('audio_upsampled.wav', 'wb')
audio_upsampled.setparams((nchannels, sampwidth, framerate * upsampling_factor, nframes, comptype, compname))

# Lee los datos del archivo original y escribe el nuevo archivo con las muestras repetidas
audio_data = audio_file.readframes(nframes)
audio_upsampled.writeframes(audio_data * upsampling_factor)

# Cierra los archivos de audio
audio_file.close()
audio_upsampled.close()
