# PEDRA - Provided Algorithms

This readme file explains the PEDRA available algorithms that can be used by setting the algorithm parameter in the config file.

# 1. Deep Q-learning (__*DeepQLearning*__)
```
file: config.cfg

algorithm:    DeepQLearning
```

Value based deep Q learning method for autonomous navigation. The input to the DNN is the image from the front facing camera, while the output is the estimated Q-value of the action in the action space. The algorithm supports
* Double DQN method
* Prioritized Experience Replay
* Distributed learning

