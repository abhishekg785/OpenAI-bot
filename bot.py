# Reinforcment learning
import gym
import universe
import random

# reinforcement learning 
def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
	# for every 15 iterations , sum the total observations and take the average
	# if lower than 0, change the direction
	# if go 15 iterations , and get the reward , that means we are getting things right
	# that is when we turn
	if j >= 15:
		if(total_sum / j) == 0:
			turn = True
		else:
		 	turn = False

		# reset vars
		j = 0
		prev_total_sum = total_sum
		total_sum = 0
	else: 
		turn = False
	if(observation_n != None):
		# increment the counter and the reward sum
		j+=1
		total_sum = reward_n
	return (turn, j, total_sum, prev_total_sum)
	

def main():
	#init environments
	env = gym.make('flashgames.CoasterRacer-v0')
	observation_n = env.reset()
	print 'making observation'
	print observation_n

	#init variables
	#no of game iterations
	n = 0
	j = 0
	# sum of observations
	total_sum = 0
	prev_total_sum = 0
	turn = False

	#define our turns or keyboard actions
	left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
	right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
	forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

	#main logic
	while True:
		# increment a counter for no of iterations
		n+=1

		# if atleast one iteration is made , check if turn is needed
		if(n > 1):
		# if at least one itreation, check if a turn
			if(observation_n[0] != None):
				# store the reward in the previous score
				prev_score = reward_n[0]

				# should we turn ?
				if(turn):
					# pick a random event
					event = random.choice([left, right])
					# perform an action
					action_n = [event for ob in observation_n]
					# set turn to false
					turn  = False
		elif(~turn):
			# if no turn is needed , go straight
			action_n = [forward for ob in observation_n]

		# if there is an observation, game has started , check if turn needed
		if(observation_n[0] != None):
			turn, j , total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])

		# save the variables for each iteration
		observation_n, reward_n, done_n, info = env.step(action_n)

		env.render()

if __name__ == '__main__':
	main()
