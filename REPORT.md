# Navigation Project report


## Introduction

The goal of the project is to train an agent to navigate a virtual large world and collect as many yellow bananas as possible while avoiding blue bananas. 

The project environment provided by Udacity is similar to, but not identical to the [Banana Collector](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#banana-collector) environment on the Unity ML-Agents GitHub page.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Given this information, the agent has to learn how to best select actions from four discrete actions:

- `0` - walk forward
- `1` - walk backward
- `2` - turn left
- `3` - turn right

The project requires that the agent must get an average score of +13 over 100 consecutive episodes. To meet the requirement, deep Q-learning (DQN) (Hassabis et al. Human-level control through deep reinforcement learning. Nature February 2015) together with experience replay and fixed Q targets are implemented. The model successfully solves the environment after 422 episodes.

## The Model

The model is implemented using torch framework.  The deep Q-learning (DQN) consists of three full connected layers

```
   fc1 = nn.Linear(state_size, h1_units),
   fc2 = nn.Linear(h1_units, h2_units),
   fc3 = nn.Linear(h2_units, action_size),
```
where state_size = 37 is the dimension of each state, action_size = 4 is the dimension of each action. h1_units is the number of nodes in the first hidden layer and h2_units is the number of the nodes in the second hidden layer. The activation function ReLU is applied to the output of fc1 and fc2. 

As in the standard DQN, the experience replay uses a replay buffer (ReplayBuffer). ReplayBuffer is implemented using namedtuple and deque of python collections

```
   memory = deque(maxlen=buffer_size) 
   experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
```
An experience is a named tuple consisting of state, action, reward, next state and done, where done flags if the terminated state is reached. 

The model can be configured differently, for example,  by choosing different unit sizes for hidden layers. Two sets of unit sizes (64, 64) and (128, 128) are tested. Both perform well and solve the environment in less then 500 episodes

## Hyper parameters

Hyper parameters used in the model are 

* Replay buffer size 100,000 
* batch size = 64
* Discount factor 0.99 (gamma)
* Soft update factor 0.001 (tau)
* Learning rate 0.0005 (alpha)
* Network update step interval 4

## Results
The model runs reasonably fast even only using CPU. The result with hidden sizes (128, 128) are presented here. The graph shows the rewards per episode 

![scores](scores.jpg)

The average scores per 100 episodes as shown as follows. The model solve the environment after 428 episodes. The agent receives average score more than 13 over the last 100 episode.  

```
Episode 100	Average Score: 0.34
Episode 200	Average Score: 2.95
Episode 300	Average Score: 7.68
Episode 400	Average Score: 9.982
Episode 500	Average Score: 12.39
Episode 528	Average Score: 13.04
Environment solve in 428 episodes!	Average Score: 13.04
```

## Conclusions

DQN performs reasonably well to achieve the goal. The model can be further improved and enhanced 

* Double DQN
* Prioritized Experience Replay
* Dueling DQN

Double DQN very likely improves DQN considerably as DQN over-estimates Q-values. Using Prioritized Experience Replay or Dueling DQN can further enhance the model. 



