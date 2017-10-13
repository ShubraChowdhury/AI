import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
from keras import layers


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
#    print(len(series),window_size,len(series)-window_size)
    for i in range(0, len(series)-window_size):
        X.append(series[i:i+window_size])
        y.append(series[i+window_size])
        
#        print('i: ',i,'X :',series[i:(i+window_size)],' y:',series[i+window_size])
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
#    print('X :-',X,' y :-', y)
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    #layer 1 uses an LSTM module with 5 hidden units (note here the input_shape = (1,window_size))
    model.add(LSTM(5,input_shape = (window_size,1)))
    #•layer 2 uses a fully connected module with one unit
    model.add(Dense(1))
    """
    https://keras.io/optimizers/ 
    RMSprop is the optimizer usually a good choice for recurrent neural networks
    keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    It is recommended to leave the parameters of this optimizer at their default values (except the learning rate, which can be freely tuned).
    """
#    optimizer=keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
#    #•the 'mean_squared_error' loss should be used (remember: we are performing regression here)
#    model.compile(loss='mean_squared_error', optimizer = optimizer)
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    
    """
    1. Get python punctuation
    """
    from string import punctuation
    """
    Below punctuation are not be removed
    """
    punctuation1 = ['!', ',', '.', ':', ';', '?']
    """
    Remove any numeric values as TODO states....
    return the text input with only ascii lowercase and the punctuation 
    """
    num_char = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    """
    Get all unique character in the supplied text
    """
    unique_chars = list(sorted(set(text)))
    
    """
    Place Holder for any special character
    """
    special_char =[]
    
    """
    All character this along with punctuation and number I will us to detect 
    special character
    """
    
    Aa =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','S','U','V','W','X','Y','Z']
    
    """
    Now I am appending python punctuation to num_char  , so it will now have
    numeric value and python punctuation
    """
    for pn in  punctuation:
        num_char.append(pn)
        
    """
    Now get special characters, check unique_chars should not be in 
    num_char , alphabets and the space between words . The rest will 
    come out as special characters
    """
        
    for uc in   unique_chars:
        if uc not in num_char and uc not in Aa and uc not in ' ':
            special_char.append(uc)
    
    """
    Now add special_char to num_char and this becomes full list of numbers,
    alphabets and special characyters
    """
    for sp in special_char:
        num_char.append(sp)
        
    """
    As per question we need to keep some punctuations listed in 
    punctuation1 so we will remove those from num_char 
    and store in punch_to_remove
    """
    punch_to_remove = [p for p in  num_char if p not in punctuation1]
    
    """
    Now remove the garbage and join nback the text 
    """
    text = ''.join([c for c in text if c not in punch_to_remove ])
    print("\n Pun Num Remove \n ", punch_to_remove)
    print("\n Special Char Remove \n ", special_char)
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    for i in range(0, len(text) - window_size, step_size):
        inputs.append(text[i:i + window_size])
        outputs.append(text[i + window_size]) 

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    
    model = Sequential()
    """
    •layer 1 should be an LSTM module with 200 hidden units -->
    note this should have input_shape = (window_size,len(chars))
    where len(chars) = number of unique characters in your cleaned text
    """
    model.add(LSTM(200, input_shape=(window_size,num_chars)))
    
    """
    •layer 2 should be a linear module, fully connected, 
    with len(chars) hidden units --> where len(chars) = number of unique 
    characters in your cleaned text
    """
    model.add(Dense(num_chars, activation='linear'))
    """
    •layer 3 should be a softmax activation ( since we are solving a
    multiclass classification)
    """
    model.add(layers.Activation('softmax'))
    
    return model
