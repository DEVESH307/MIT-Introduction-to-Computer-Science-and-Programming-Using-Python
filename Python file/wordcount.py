import time
import multiprocessing

def inputs(str):
	with open("C:\\Users\\djaiswal\\Downloads\\InputOutput.txt",'a+') as f:
		for 
		lock.acquire()
	    time.sleep(0.01)
	    lock.release()

def outputs(str):
	with open("C:\\Users\\djaiswal\\Downloads\\InputOutput.txt",'r') as f:
	counts = dict()
    words = f.split()
    time.sleep(0.01)
    lock.acquire()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
	    lock.release()
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=inputs, args=(inputs,lock))
    w = multiprocessing.Process(target=outputs, args=(outputs,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    # print(balance.value)



def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
 str(T2) = word_count("I am good")
print (T2)
