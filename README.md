# LT2222 V21 Assignment 3

Your name: Minerva (gussuvmi)

## Part 1
explain what the functions a, b, and g do, as well as the meaning of the command-line arguments that are being processed via the argparse module.

a(f)
f = filepath
open file, loop through its lines, for every line in the file (NOPE append a new list to the list mm) add the tokens of the line to the list mm (so "extend" the list with the tokens of the sentence) 
after this add two "<s>"-tokens to the beginning of the list mm and two "<e>" tokens to the end of the list -> you will have a list of all the tokens in the file. The return result will be a two element tuple where the first element is the list mm and the second element is a set (as a list) of the tokens

b(u, p)
u and p are a result from function a, so
u = all tokens in the text
p = a set of the tokens (unique tokens)/vocabulary
gt = list of vowel indices
gr = list of what
loop through the range from 0 to lenght of all tokens minus 4 (why minus 4? -> to avoid out od index error maybe?)
on every round inspect the element at i+2 position. If this element is not a vowel, dont continue to the next part. 
Next part: get the token from "all tokens"- list with the current index -> so the letter previous to the vowel and then the next two letters after the vowel. For each of these 3 tokens, call the function g(x, p) which will return an array for each token, the result will be concatented into a single array. (so r will be an array of zeros, the length of the vocabulary and in place of each of the three letters there will be 1 eg if the vocabsize is 5 [0,1,0,1,1])
After each iteration return a tuple where the first element is a numpy array of the list gr and the seconf element a numpy array of the list of vowel indices. np.array(gr), np.array(gt)

g(x, p)
x = a letter
p = vocabulary/unique letters
create a vector/array of zeros, of the length of the vocabulary
set the value at the index where x exists in the vocabulary to 1
return the array

command-line args:
m = training file path
h = path to save model to
k = (optional) hiddensize, what is this??, default value is 200
r = (optional) epochs, default value 100

train:
finally use the train function from the file model.py to train a model. The train function takes as arguments the weird array of arrays with many zeros and one's for the preceding and succeeding letters, the array of vowel indices, the vocabulary/set of unique letters, and from the command line arguements hiddensize k and epochs r. The train function returns a model which is then saved to the file path specified in the command line arguments.


>> python3 train.py
usage: train.py [-h] [--k K] [--r R] m h
train.py: error: the following arguments are required: m, h
dest - The name of the attribute to be added to the object returned by parse_args().???

## Part 2

## Part 3

## Bonuses

## Other notes
