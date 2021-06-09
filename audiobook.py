#pip install pyttsx3, PyPDF2
import pyttsx3
#import PyPDF2

#book = open('RichDadPoorDad.pdf','r')
#pdfReader = PyPDF2.PdfFileReader(book)
#pages = pdfReader.numPages
#print(pages)

speaker = pyttsx3.init()
data = open("demotext.txt", 'r')

text = data.read()
print(text)
speaker.say(text)
speaker.say("Yeah we are done!! Thank you for listening me, see you later byeee")
speaker.runAndWait()
data.close()


'''
for num in range(2,pages):
    page = pdfReader.getPage(12)
    text = page.extractText()

    speaker.say(text)
    speaker.runAndWait()
'''    