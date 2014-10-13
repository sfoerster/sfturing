

class sfturing:

	
	def __init__(self,q_0,q_a,q_r,delta,tape,**kwargs):
		self.delta   = delta
		self.q_a	 = q_a
		self.q_r	 = q_r

		self.currentState = q_0

		self.options = {'no_delta': 'reject',
						'max_steps': 10000,
						'clone_tape': kwargs.get('clone_tape', False)}

		if len(self.delta) < 1:
			raise Exception('delta cannot be empty')

		# the deltas determine if this is a multi-tape machine
		self.headidx = [0] * (len(self.delta.keys()[0])-1)

		self.tape    = [['b']] * (len(self.delta.keys()[0])-1)
		self.tape[0] = tape
		self._tapeChanged(0)

		# ensure the input ends with a 'b'
		if self.tape[0][-1] is not 'b':
			self.tape[0].append('b')
			self._tapeChanged(0)


	def run(self):

		n=0
		while self.currentState is not self.q_a and self.currentState is not self.q_r:
			
			if n > self.options['max_steps']:
				raise Exception('Max steps exceeded: '+str(self.options['max_steps']))

			self._stateString()
			self._nextState()
			n += 1

		self._stateString()

		if self.currentState is self.q_a:
			print 'ACCEPTED!'
			return 0

		print 'REJECTED!'
		return 1

	def _nextState(self):

		idx = tuple([self.currentState]+[self.tape[n][self.headidx[n]] for n in xrange(len(self.headidx))])

		data = [k for v,k in self.delta.items() if v == idx]
		#data = delta[idx]
		if not data:
			#raise Exception('No delta recorded for case: '+repr(idx))
			self._noDelta(repr(idx))
		if len(data)>1:
			raise Exception('Too many deltas recorded for case: '+repr(idx))

		data = data[0]

		nextState = data[0]

		if (len(data)-1) % 2 is not 0:
			raise Exception('Illegal entries in the delta: must be odd but is: '+repr(data))

		numTapes = (len(data)-1)/2

		writes = data[1:numTapes+1] # the first numTapes entries after state
		moves  = data[-numTapes:] # the last numTapes entries

		for n in xrange(numTapes):
			self.tape[n][self.headidx[n]] = writes[n]
			self._tapeChanged(n)

			if self.headidx[n] is not 0 and moves[n] is 'L':
				self.headidx[n] -= 1

			if moves[n] is 'R':
				self.headidx[n] += 1
				if self.headidx[n] is len(self.tape[n]):
					self.tape[n].append('b')
					self._tapeChanged(n)

		self.currentState = nextState

	def _tapeChanged(self, idx):

		if self.options['clone_tape']:
			mtape = self.tape[idx]
			for n in xrange(len(self.tape)):
				self.tape[n] = mtape

	def _stateString(self):

		for n in xrange(len(self.tape)):
			print 'tape '+str(n)+': '+''.join(self.tape[n][:self.headidx[n]]) + '{q_' + str(self.currentState) + '}' + ''.join(self.tape[n][self.headidx[n]:])


	def _noDelta(self,badidx=''):

		if self.options['no_delta'] == 'reject':
			print 'No delta defined: '+badidx
			print 'REJECTED!'
			return 1

		raise Exception('No delta defined: Unrecognized no_delta option: '+badidx)