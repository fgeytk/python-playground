class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','').replace("'",' ')

        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
    def mostFrequentWord(self):
        # get frequency map
        freqDict = self.freqAll()
        
        # Find the word with the maximum frequency
        mostFrequent = max(freqDict, key=freqDict.get)
        return mostFrequent, freqDict[mostFrequent]
        


analyzed = TextAnalyzer("They ,Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing.")
print(analyzed.freqAll())
print(analyzed.mostFrequentWord())
