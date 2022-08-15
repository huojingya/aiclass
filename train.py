# Imports here
#%matplotlib inline
#%%config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from PIL import Image
import numpy as np

def main(data_directory):
    in_args = get_input_args()

def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type = str, default = './')
    parser.add_argument('--arch',type = str, default = 'vgg13')
    parser.add_argument('--learning_rate',type = float, default = 0.003)
    parser.add_argument('--epochs',type = int, defulat = 20)
    parser.add_argument('--gpu',type = bool, default = False)
    
    
    in_args = parser.parse_args()
    
    return in_args