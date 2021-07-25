import pyttsx3



class playaudio:
    def __init__(self,voice='female',speakerstatus=True):
        self.voice='female'
        self.speakstatus=speakerstatus
        self.speakwords={
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '0': 'zero',
            '+': 'plus',
            '-': 'minus',
            '=': 'equal to',
            'x': 'multiply',
            '/': 'divide',
            '%': 'mod',
            '^': 'power',
            'x!': 'factorial',
            'sqrt': 'square root'
        }

        self.engine=pyttsx3.init()
        v=self.engine.getProperty('voices')
        self.engine.setProperty("voice",v[1].id)


    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakwords[content])
            self.engine.runAndWait()
if __name__ == '__main__':
    ob=playaudio()
    ob.speak('1')


