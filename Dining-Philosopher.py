#Marisol Morales, Student ID: 029984979, Due Date: 3/9/2025
#import our needed libraries
import threading
import time
import random 

#define our number of philosophers and our forks 
num_philo = 5
num_forks = num_philo

#now lets define our needed semaphores for the forks along for our mutex!
forks = [threading.Semaphore(1) for i in range(num_forks)]
mutex = threading.Semaphore(1)

#make our pickup_fork function this is for the philosopher to pick up the forks
def pickup_fork(index):
    mutex.acquire()
    left_fork = index
    right_fork = (index + 1) % num_forks

    forks[left_fork].acquire()
    forks[right_fork].acquire()

    print(f"Philosopher {index} picked up forks {left_fork} and {right_fork}, they are eating.")

    mutex.release()

#making our return forks function which allows the philosopher to release the forks for others to pick up and use
def return_forks(index):
    left_fork = index
    right_fork = (index + 1) % num_forks

    forks[left_fork].release()
    forks[right_fork].release()

    print(f"Philosopher {index} has put down the following forks, {left_fork} and {right_fork}")

#defining our philosopher thread function 
def philosopher(index):
    while True:
        print(f"Philosopher {index} is thinking...")
        #put our philosopher to sleep (this is what helps us stimulate the action of thinking)
        time.sleep(random.randint(1,3))
        #now we call for our pickup fork function that allows us to have the philosopher eat
        pickup_fork(index)
        #we then put the same one to sleep as this is what helps us stimulate the action of eating now
        time.sleep(random.randint(1,3))
        #now we have them put down the forks/finish up eating allowing for other philosophers to eat
        return_forks(index)

#create our philosopher threads with a for loop
threads = []
for i in range(num_philo):
    thread = threading.Thread(target=philosopher, args=(i,)) #similar to how you approach this in C++
    threads.append(thread)

#start our philosopher threads using a for loop
for thread in threads:
    thread.start()

#now we join our threads together
for thread in threads:
    thread.join()