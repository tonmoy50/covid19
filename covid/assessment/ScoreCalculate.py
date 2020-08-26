import numpy as np

#data = {'name' : 'Tonmoy', 'age' : 'abc', 'sex' : 'male', 'temp' : 100}
#symptom = {'breathing' : None, 'cough' : 'cough', 'soar' : 'soar', 'weakness' : None, 'nose' : None}
#add_symptom = {'abdominal' : 'abdominal', 'vomit' : None, 'diarrhoea' : None, 'chest_pain' : 'chest_pain', 'muscle' : None, 'loss_taste' : 'loss_taste', 'rash' : 'rash', 'loss_speech' : None}

class ScoreCalculate:
    
    def __init__(self, data, symptom, add_symptom):
        
        self.data = {}
        self.symptom = {}
        self.add_symptom = {}
        self.score = 0

        self.data = data
        self.symptom = symptom
        self.add_symptom = add_symptom


    def calculate(self):

        try:
            self.data['temp'] = float(self.data['temp'])
        except ValueError:
            return "TemperatureError"
        
        if self.data['temp'] > 100.9:
            self.score = self.score + 2
        
        sym_count = 0
        
        for items in self.symptom:
            if(self.symptom[items] != None):
                sym_count = sym_count + 1
                if sym_count == 1:
                    self.score = self.score + 3
                else:
                    self.score = self.score + 1
        
        for items in self.add_symptom:
            if(self.add_symptom[items] != None):
                self.score = self.score + 2

        


        return self.score
