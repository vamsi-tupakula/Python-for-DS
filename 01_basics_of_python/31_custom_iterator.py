class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

my_sen = Sentence('This is a Python Program')

print(next(my_sen))

def sentence_gen(sentence):
    for word in sentence.split():
        yield word
    
gen_sen = sentence_gen('This is Jhonny Depp')
print(next(gen_sen))
print(next(gen_sen))
print(next(gen_sen))
print(next(gen_sen))