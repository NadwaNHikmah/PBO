from gtts import gTTS 
from playsound import playsound

mytext = 'Selamat Datang di Fakultas Teknik! Namaku Nadzwa Nurul Hikmah dari Teknik Informatika'
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("selamat_datang.mp3") 
playsound("selamat_datang.mp3", True)