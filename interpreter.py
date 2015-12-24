from subprocess import call
from multiprocessing import Pool
import signal

def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

pool = Pool(1, init_worker)

def interpret(query):
	if query == 'spotify':
		call(["pytify"])
	elif query == 'next song':
		call(['pytify', '-n'])
	elif query == 'previous song':
		call(['pytify', '-p'])
	elif query == 'pause' or query == 'play':
		call(['pytify', '-pp'])
	elif query == 'date':
		say('Today is')
		call(['date'])

def say(line):
	try:
		pool.map_async(say, ('hello chris, how are you today?',))
		
	except (KeyboardInterrupt, EOFError):
		return