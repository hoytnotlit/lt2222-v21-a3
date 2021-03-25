import argparse
import torch
import train
import pandas as pd
import numpy as np

vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o'])

def load_data(f):
    mm = []
    with open(f, "r") as q:
        for l in q:
            mm += [c for c in l]

    mm = ["<s>", "<s>"] + mm + ["<e>", "<e>"]
    return mm, list(set(mm))

def load_train_vocab(f):
    mm = []
    with open(f, "r") as q:
        for l in q:
            mm += [c for c in l]

    mm = ["<s>", "<s>"] + mm + ["<e>", "<e>"]
    return list(set(mm))

def get_feature(token, vocab, vocab_len):
    z = np.zeros(vocab_len)
    z[vocab.index(token)] = 1
    return z

def get_test_instances(data, vocab, vocab_len):
    classes = []
    features = []
    for v in range(len(data) - 4):
        if data[v+2] not in vowels:
            continue
        
        h2 = vowels.index(data[v+2])
        classes.append(h2)
        feat = np.concatenate([get_feature(x, vocab, vocab_len) for x in [data[v], data[v+1], data[v+3], data[v+4]]])
        features.append(feat)

    return np.array(features), np.array(classes)

def get_instances(data, vocab, train_data):
    # load the vocab from train data to use for feature lengths to make testing instances compatible
    # with training instances
    train_vocab = load_train_vocab(train_data)
    X, y = get_test_instances(data, vocab, len(train_vocab)) # create evaluation instances

    # create tensor from dataframe
    df = pd.DataFrame(X)
    df['class'] = y
    featuredf = df.drop('class', axis=1)
    classdf = df['class']
    tensor = torch.Tensor(featuredf.to_numpy()), torch.LongTensor(classdf.to_numpy())

    return tensor
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str)
    parser.add_argument("test_data", type=str)
    parser.add_argument("train_data", type=str)
    parser.add_argument("output_file", type=str)
    
    args = parser.parse_args()

    model = torch.load(args.model) # load a model produced by train.py
    model.eval()

    data, vocab = load_data(args.test_data) # load the test data
    testing_instances, actual_classes = get_instances(data, vocab, args.train_data)
    outputs = model(testing_instances.unsqueeze(0)) # predict instances
    predictions = pd.Series(outputs.squeeze(0).argmax(dim=1).numpy())
    # actual_df = pd.DataFrame(actual_classes)
    actual = pd.Series(actual_classes)

    # Write the text with the predicted (as opposed to the real) vowels back into an output file.
    new_text = []
    next_index = 0
    for token in data:
        if token in vowels:
            new_text.append(vowels[predictions[next_index]])
            next_index = next_index + 1
        else:
            new_text.append(token)

    with open(args.output_file, "w") as new_file:
        new_file.write(''.join(new_text))

    # correct_predictions = 0
    # for item in zip(predictions.to_list(), actual.to_list()):
    #     if item[0] == item[1]:
    #         correct_predictions = correct_predictions + 1

    # print(len(actual[predictions == actual]))
    # print(correct_predictions)
    
    # Print the accuracy of the model to the terminal
    accuracy = len(actual[predictions == actual]) / len(actual)
    print(f"Model accuracy is {accuracy}")