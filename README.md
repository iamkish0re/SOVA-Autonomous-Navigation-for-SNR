# Autonomous Navigation System

In this project, we have developed an autonomous navigation system that uses a deep reinforcement learning model to navigate a drone. We trained the model in AirSim, and then used transfer learning to apply the model to a real drone. The system also includes a GUI-based path planning tool and hand gesture controls.

## Dataset

We used the AirSim simulator to collect training data for our deep reinforcement learning model. The dataset consists of simulated drone flight paths, along with the corresponding rewards for each action taken by the drone.

## Libraries Used

We used the following libraries to develop our autonomous navigation system:

- TensorFlow
- Keras
- AirSim
- OpenCV

## System Architecture

Our autonomous navigation system consists of the following components:

- Deep reinforcement learning model: This model was trained in AirSim using the training dataset, and then fine-tuned for real-world drone navigation using transfer learning.
- Path planning tool: This tool allows the user to draw a path on a GUI, which is then used by the drone to navigate to the destination.
- Hand gesture controls: The system also includes hand gesture controls, which allow the user to control the drone's movements using hand gestures.

## Analysis

We evaluated the performance of our autonomous navigation system by testing it on a real drone in various indoor and outdoor environments. The system was able to successfully navigate the drone to its destination in most cases, and the hand gesture controls provided an intuitive and easy-to-use interface for controlling the drone's movements.

## Conclusion

Our autonomous navigation system demonstrates the power and potential of deep reinforcement learning for drone navigation. The combination of a deep reinforcement learning model, transfer learning, and a path planning tool provides a robust and versatile system for drone navigation, while the hand gesture controls provide a user-friendly interface that can be used by anyone, regardless of their technical expertise. We hope that this system will contribute to the development of more advanced and intelligent autonomous drone systems in the future.
