import gym
envout = gym.make("Taxi-v2").env
state = envout.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
envout.s = state
envout.render()
envout.P[328]
print("Action Space {}".format(envout.action_space))
print("State Space {}".format(envout.observation_space))
print("State:", state)