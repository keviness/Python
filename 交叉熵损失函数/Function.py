import numpy as np


def CrossEntropy_loss(y_true:list,y_pred:list):
    
    assert len(y_true)==len(y_pred)
    loss=0
    for y,fx in zip(y_true,y_pred):
        loss+=-y * np.log(fx)
    return loss
    
if __name__ == '__main__':
    px=[0.1,0.2,0.7]
    py=[0.3,0.3,0.4]
    loss = CrossEntropy_loss(px,py)
    print('loss:\n', loss)