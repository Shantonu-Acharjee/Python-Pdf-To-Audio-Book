from gtts import gTTS
import os
from playsound import playsound
import PyPDF2
pdfReader=PyPDF2.PdfFileReader(open('About Bangladesh.pdf','rb'))
pages=pdfReader.numPages
print('Total Pages is : ',pages)
for num in range(1,pages):
    page = pdfReader.getPage(num)
    Text1 = page.extractText()

    language = 'en'
    myobj = gTTS(text=Text1, lang=language, slow=False)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')
    os.remove('welcome.mp3')
