'''

Full Project Link : https://github.com/ShantonuAcharjee/Python-Pdf-To-Audio-Book
Author: Shantonu Acharjee
Email: shantonuacharjee@gmail.com
YouTube :- http://tinyurl.com/yy374bou
FaceBook: http://tinyurl.com/y52rgdd4

'''
import pyttsx3
import PyPDF2
pdfReader=PyPDF2.PdfFileReader(open('About Bangladesh.pdf','rb'))
pages=pdfReader.numPages
print('Total Pages is : ',pages)
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)# change the number of 'voices[].id' for change voice
for num in range(1,pages):
    page=pdfReader.getPage(num)
    Text1=page.extractText()
    engine.say(Text1)
    print('The mumber of Page I read now :',num)
    engine.runAndWait()
