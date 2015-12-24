from subprocess import call
from interpreter import interpret
from multiprocessing import Pool
from multiprocessing import Process
from sys import exit
import signal

class Macsy:
	def __init__(self):
		self.run()

	def run(self):
		pool.map_async(say, ('hello chris, how are you today?',))
		while(True):
			query = raw_input('> ')
			pool.map_async(say, (query,))
			if query == 'exit':
				call(["say", "See you next time."])
				break
			elif query == 'bye':
				call(["say", "It's been a pleasure."])
				break
			interpret(query)

def say(line):
	try:
		call(["say", line])
	except (KeyboardInterrupt, EOFError):
		return

def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

if __name__ == '__main__':
	pool = Pool(2, init_worker)
	try:
		Macsy()

	except (KeyboardInterrupt, EOFError):
		pool.map_async(say, ('Bye',))
		print('\nmacsy>closing...\n')
		pool.close()
		pool.join()
		exit(1)