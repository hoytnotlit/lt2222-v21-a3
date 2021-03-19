import argparse
import torch
import train
import pandas as pd

# def load_data(file):
#     # TODO not sure what to do here
#     text_rows = []
#     with open(file, "r") as f:
#         text_rows = [line for line in f]
#     return text_rows


def get_instances(test_data):
    # data = load_data(args.test_data) 
    data, vocab = train.a(test_data) # Load the test data

# tensor([[[0., 0., 0.,  ..., 0., 0., 0.],
#          [0., 0., 0.,  ..., 0., 0., 0.],
#          [0., 0., 0.,  ..., 0., 0., 0.],
#          ...,
#          [0., 0., 0.,  ..., 0., 0., 0.],
#          [0., 0., 0.,  ..., 0., 0., 0.],
#          [0., 0., 0.,  ..., 0., 0., 0.]]])
    # torch.Tensor()

    instances = train.b(data, vocab) # Create evaluation instances compatible with the training instances.  
    # (A simplifying assumption for the purposes of the assignment: assuming that the neighbouring 
    # vowels are known as though the Fairy hadn't stolen them.)
    df = pd.DataFrame(instances[0])
    # df['class'] = instances[1]
    # featuredf = df.drop('class', axis=1)
    # classdf = df['class']
    tensor = torch.Tensor(df.to_numpy())
    # tensor = torch.Tensor(featuredf.to_numpy()), torch.LongTensor(classdf.to_numpy())
    # print(tensor.unsqueeze(1))
    return tensor.unsqueeze(1)
    

if __name__ == "__main__":
    # What eval.py will do from the command line:

    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str)
    parser.add_argument("test_data", type=str)
    
    args = parser.parse_args()

    model = torch.load(args.model) # Load a model produced by train.py

    instances = get_instances(args.test_data)
    # predictions = model(instances[0]) # Use the model to predict instances
    # Write the text with the predicted (as opposed to the real) vowels back into an output file.
    # f = open("predictions.txt", "w")
    # f.write(predictions)
    # f.close()
    # Print the accuracy of the model to the terminal.

    # https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html