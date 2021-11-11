# Statistics-on-the-Escalator
In this paper, I tried to create an interesting model for describing the movement of people on an escalator. It would be interesting to understand why people are forced to stand on both sides of the escalator, and not walk on it.

To describe a simple case, let's choose a model in which the escalator does not move. Let's say we have numbers from 1 to L (where L is the length of the escalator) that correspond to the step number. And let's say that there is a discrete time in the problem. Let's say that people appear with probability α in position one if there is no one there at the moment. Further, at each moment of time, each person, if there is no one after him, then he moves forward one step with a probability of p. Then the interesting question is what will be the capacity of such an escalator. Exactly, how many people get off the escalator per unit of time. This happens in the file [without_speed_model.py](without_speed_model.py).
