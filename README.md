# LT2222 V21 Assignment 3

Your name: Minerva (gussuvmi)

## Part 1
Explain what the functions a, b, and g do, as well as the meaning of the command-line arguments that are being processed via the argparse module.

### a(f)
Arguments:
* f = filepath

Open a text file and create a list of all the tokens (by token from here on out I mean a single letter, number or punctuation) in the file. Add two start-tokens in the beginning of the list and two end-tokens at the end of the list. 

Return:

A tuple where the first element is a list of all tokens and the second element is a list of unique tokens in the file.

### g(x, p)
Arguments:
* x = a single token
* p = unique tokens/vocabulary

Create an array of zeros of the length of the vocabulary. Set the value to 1 at the index where the given token x exists. 

Return:
An array of zeros and a one. This array is concatenated into a feature vector for a vowel.

### b(u, p)
Arguments:
* u = list of all tokens in the text
* p = list of unique tokens in the text (or the vocabulary)

Loop through all tokens. To do this loop the range from 0 to length of token list minus 4 (to avoid out of range error when checking for next two tokens) and access the n + 2 element in the token list. The last two tokens are end-tokens and they will not be checked, neither will the first two, which are start-tokens.

On every iteration check if the token is a vowel. If not, continue to next iteration. In case of a vowel, do the following:

1. Append to the initialised list *gt* the index of the current vowel in the vowels-list defined outside the function.
2. For the two preceding tokens and two succeeding tokens of the current vowel, call the function g and concatenate the return values into a single array. This will be the feature vector of the current vowel. The feature vector is an array of mostly zeros but at the index of the preceding and succeeding tokens the value will be 1. Append the feature vector to the intialised list *gr*.

Return:

A tuple where the first element is a 2d-numpy array of vowel feature vectors and the second element is a 1d-numpy array of actual classes

### command-line arguments
* m = path for training file
* h = path to save resulting model to
* k = (optional) hiddensize, size of the output features, default value is 200
* r = (optional) epochs, default value 100

### main
In the main-block of the code the command-line arguments are processed and functions a and b are run. After this the train-function from the module model.py is used to train a model. The train-function takes as arguments feature vectors and their actual classes (vowels), the vocabulary, hiddensize, and epochs. The train-function returns a model which is finally saved to the specified file path.


## Part 2
Usage: eval.py [-h] model test_data train_data output_file

Aarguments:
* model: the path of the model to evaluate
* test_data: the data to test on
* train_data: the original training data (explained below)
* output_file: file path to save predicted text to

A notable comment on the design choice of eval.py was taking the training data as a positional argument. This is because the feature vectors need to be the length of the training vocabulary, other wise there will be an error with incompatible sizes (RuntimeError: mat1 and mat2 shapes cannot be multiplied (66282x400 and 452x200)). 

## Part 3
Train:

Five different variations of the --k option, holding the --r option at its default.

    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_hiddensize_50.pt --k=50
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_hiddensize_100.pt --k=100
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_hiddensize_250.pt --k=250
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_hiddensize_300.pt --k=300
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_hiddensize_500.pt --k=500

Five different variations of the --r option, holding the --k option at its default.

    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_epoch_200.pt --r=200
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_epoch_300.pt --r=300
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_epoch_500.pt --r=500
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_epoch_750.pt --r=750
    python3 train.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt model_epoch_1000.pt --r=1000

Evaluate:

    python3 eval.py model_hiddensize_50.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_hsz_50.txt
    python3 eval.py model_hiddensize_100.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_hsz_100.txt
    python3 eval.py model_hiddensize_250.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_hsz_250.txt
    python3 eval.py model_hiddensize_300.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_hsz_300.txt
    python3 eval.py model_hiddensize_500.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_hsz_500.txt
    python3 eval.py model_epoch_200.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_e_200.txt
    python3 eval.py model_epoch_300.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_e_300.txt
    python3 eval.py model_epoch_500.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_e_500.txt
    python3 eval.py model_epoch_1000.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_e_1000.txt
    python3 eval.py model_epoch_750.pt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtrain.lower.txt predictions_e_750.txt
    
    Model accuracy is 0.13309797531758244
    Model accuracy is 0.12324613017108717
    Model accuracy is 0.1189161461633626
    Model accuracy is 0.13323375878820795
    Model accuracy is 0.1364925620832202
    Model accuracy is 0.16834132947104793
    Model accuracy is 0.12480009655713467
    Model accuracy is 0.14534866177846173
    Model accuracy is 0.16290999064602757
    Model accuracy is 0.13439546181467066


The model which had the highest accuracy is the one that was trained with 200 epochs and this is the model and the predictions that I have included in my repository.

One observation I made from the most succesful text was that the word "och" seemed to be predicted quite well. With the help of grep and wc in the command line I found out that the predictions_e_200.txt file contained 882 instances of the word "och" and the total amount of "och" in the original testing test was 1152. So at least this model was pretty decent at guessing that word(accuracy of 0.765625). In comparison the output of least accurate model predictions_hsz_250.txt contained 126 instances of the word "och" but instead had 728 instances of "ech". Similarly in some other results the majority of "och" words was guessed with the same vowel so as ech, åch, öch etc... So the model predicted the correct pattern for "och" in most cases but with the wrong vowel. Some other files had a lot of mix with different vowels for "och".

The same behaviour repeats at least for the words "jag" but in predictions_e_200.txt it is instead "jög" (67/80 cases), "den" (419/909 cases), and "en" as "on" (365/378). My guess is that frequent words and stop words are much more likely to be predicted correctly because they occur more often providing the model with more data on these words.

## Bonuses

## Other notes
