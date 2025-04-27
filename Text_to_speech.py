# Text to Speech

from gtts import gTTS


import os

# The text that you want to convert to audio
mytext = 'Hello, Everyone! welcome to the world of python programming and machine learning and data science.' \
'I am Bhupendra Bairwa. I am a student of B.Tech in Artificial Intelligence and Data Science.'


# Language in which you want to convert
language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")
Output
