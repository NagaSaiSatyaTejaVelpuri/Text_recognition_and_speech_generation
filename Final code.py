import os
from gtts import gTTS

language='en'
output=gTTS(text="wake up    wake up    wake up", lang=language,slow=False)
output.save("output2.mp3")
os.system("start output2.mp3")
