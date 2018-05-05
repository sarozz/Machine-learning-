from numpy import *
import matplotlib.pyplot as plt
def gradient_step_runner(current_theta0, current_theta1,points,learning_rate):
	gradient_theta0=0
	gradient_theta1=0
	N= float(len(points))

	for i in range(0, len(points)):
		x= points[i,0]
		y= points[i,1]
		gradient_theta0 += -(2/N)*(y-((current_theta0*x) + current_theta1))
		gradient_theta1 += -(2/N)*x *(y-((current_theta0*x) + current_theta1))
		new_theta0 = current_theta0 - (learning_rate * gradient_theta0)
		new_theta1 = current_theta1 - (learning_rate * gradient_theta1)
		return [new_theta0, new_theta1]

def gradient_descent_runner(points,learning_rate,initial_theta0,initial_theta1,number_iteration):
	current_theta0= initial_theta0
	current_theta1= initial_theta1
	for i in range(number_iteration):
 	 	current_theta0, current_theta1 =gradient_step_runner(current_theta0, current_theta1, array(points), learning_rate)
 	
 	return [current_theta0, current_theta1]


def run():
	points = genfromtxt('data.csv',  delimiter=",")

	x = []
	y = []

	for i in range(len(points)):
		x.append(points[i,0])
		y.append(points[i,1])
	plt.scatter(x,y)
	



	learning_rate= 0.001
	initial_theta0= 0
	initial_theta1= 0
	number_iteration = 76
	[theta0, theta1]= gradient_descent_runner(points, learning_rate, initial_theta0, initial_theta1,number_iteration) 
	
	linear_line = [theta1* i + theta0 for i in x]

	plt.plot(x,linear_line,'r')
	plt.show()
	
	print(theta0)
	print(theta1)
	print("Starting gradient descent at b = {0}, m = {1}".format(initial_theta0, initial_theta1))
    #print("Running...")
    #[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    #print("After {0} iterations b = {1}, m = {2}".format(number_iteration, initial_theta0, initial_theta1))



if __name__ == '__main__':
     run()