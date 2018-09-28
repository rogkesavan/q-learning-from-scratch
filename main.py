import gym
envout = gym.make("Taxi-v2").env
state = envout.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
envout.s = state
envout.render()
envout.P[328]
env.s = 328
epoch = 0
penalties, reward = 0, 0
frames = [] #for anniamation 
done = False 
#We'll create an infinite loop which runs until one
#  passenger reaches one destination (one episode), or in other words, when 
# the received reward is 20. The env.action_space.sample()
while not done:
    action = envout.action_space.sample()
    state, reward, done, info = envout.step(action)
    if reward == -10:
        penalties += 1
print("Action Space {}".format(envout.action_space))
print("State Space {}".format(envout.observation_space))
print("State:", state)