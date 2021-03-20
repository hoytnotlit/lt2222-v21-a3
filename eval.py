import argparse
import torch
import train
import pandas as pd


def get_instances(test_data):
    # TODO should use training data for feature lengths..?
    # data = load_data(args.test_data) 
    data, vocab = train.a(test_data) # Load the test data
    # tensor([[[0., 0., 0.,  ..., 0., 0., 0.],
    #      [0., 0., 0.,  ..., 0., 1., 0.],
    #      [0., 0., 0.,  ..., 0., 0., 0.],
    #      ...,
    #      [0., 0., 0.,  ..., 0., 0., 0.],
    #      [0., 0., 0.,  ..., 0., 0., 0.],
    #      [0., 0., 0.,  ..., 0., 0., 0.]]])
    # y = []
    # X = []
    # vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o'])
    # print(len(p))
    
    # z = np.zeros(113)
    # z[p.index(x)] = 1

    # for v in range(len(data) - 4):
    #     if data[v+2] not in vowels:
    #         continue
        
    #     h2 = vowels.index(u[v+2])
    #     y.append(h2)
    #     r = np.concatenate([g(x, p) for x in [data[v], data[v+1], data[v+3], data[v+4]]])
    #     X.append(r)

    # np.array(X), np.array(y)

    X, y = train.b(data, vocab) # Create evaluation instances compatible with the training instances.  
    # (A simplifying assumption for the purposes of the assignment: assuming that the neighbouring 
    # vowels are known as though the Fairy hadn't stolen them.)
    df = pd.DataFrame(X)
    df['class'] = y
    featuredf = df.drop('class', axis=1)
    classdf = df['class']
    tensor = torch.Tensor(df.to_numpy())
    tensor = torch.Tensor(featuredf.to_numpy()), torch.LongTensor(classdf.to_numpy())
    return tensor
    

if __name__ == "__main__":
    # What eval.py will do from the command line:

    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str)
    parser.add_argument("test_data", type=str)
    
    args = parser.parse_args()

    model = torch.load(args.model) # Load a model produced by train.py
    model.eval()

    testing_instances, actual_classes = get_instances(args.test_data)
    outputs = model(testing_instances.unsqueeze(0)) # Use the model to predict instances
    predictions = pd.Series(outputs.squeeze(0).argmax(dim=1).numpy())

    # print(train.vowels)
    # Write the text with the predicted (as opposed to the real) vowels back into an output file.
    # f = open("predictions.txt", "w")
    # f.write(predictions)
    # f.close()
    # Print the accuracy of the model to the terminal.

    # https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html