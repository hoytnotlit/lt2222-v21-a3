# LT2222 V21 Assignment 3

Your name: Minerva (gussuvmi)

## Part 1
Explain what the functions a, b, and g do, as well as the meaning of the command-line arguments that are being processed via the argparse module.

**a(f)**
Arguments:
*f = filepath*

Open a text file and create a list of all the tokens in the file. Add two start-tokens in the beginning of the list and two end-tokens at the end of the list. 

Return:
A tuple where the first element is a list of all tokens and the second element is a list of unique tokens in the file.

<!-- open file, loop through its lines, for every line in the file (NOPE append a new list to the list mm) add the tokens of the line to the list mm (so "extend" the list with the tokens of the sentence) 
after this add two "<s>"-tokens to the beginning of the list mm and two "<e>" tokens to the end of the list -> you will have a list of all the tokens in the file. The return result will be a two element tuple where the first element is the list mm and the second element is a set (as a list) of the tokens -->

**b(u, p)**
Arguments:
<!-- u and p are a result from function a, so -->
*u = list of all tokens in the text*
*p = list of unique tokens in the text (or the vocabulary)*

TODO write better
gt = list of vowel indices
gr = list of what
loop through the range from 0 to lenght of all tokens minus 4 (why minus 4? -> to avoid out of index error maybe?)
on every round inspect the element at i+2 position. If this element is not a vowel, dont continue to the next part. 
Next part: get the token from "all tokens"- list with the current index -> so the letter previous to the vowel and then the next two letters after the vowel. For each of these 3 tokens, call the function g(x, p) which will return an array for each token, the result will be concatented into a single array. (so r will be an array of zeros, the length of the vocabulary and in place of each of the three letters there will be 1 eg if the vocabsize is 5 [0,1,0,1,1])
After each iteration return a tuple where the first element is a numpy array of the list gr and the seconf element a numpy array of the list of vowel indices. np.array(gr), np.array(gt)

**g(x, p)**
*x = a single token*
*p = unique tokens/vocabulary*

Create an array of zeros of the length of the vocabulary. Set the value to 1 at the index where the given token x exists. 

Return:
An array of zeros and a one. This array is concatenated into a feature vector for a vowel.

**command-line arguments**
m = path for training file
h = path to save resulting model to
k = (optional) hiddensize, TODO what is this??, default value is 200
r = (optional) epochs, default value 100

**main**
In the main-block of the code the command-line arguments are processed and functions a and b are run. After this the train-function from the module model.py is used to train a model. The train-function takes as arguments feature vectors and their actual classes (vowels), the vocabulary, hiddensize, and epochs. The train-function returns a model which is finally saved to the specified file path.


<!-- >> python3 train.py
usage: train.py [-h] [--k K] [--r R] m h
train.py: error: the following arguments are required: m, h
dest - The name of the attribute to be added to the object returned by parse_args().??? -->

## Part 2

## Part 3

## Bonuses

## Other notes
