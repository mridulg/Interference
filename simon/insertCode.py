if expInfo['counterbalance']=='0':
	bindings = {'X':'m', 'O':'z'}
	if thisTrial['condition']=='incongruent' and thisTrial['stim']=='X':
		leftStimText = thisTrial['stim']
		rightStimText = ''
		ans = 'm'
	elif thisTrial['condition']=='incongruent' and thisTrial['stim']=='0':
		rightStimText = thisTrial['stim']
		leftStimText = ''
		ans = 'z'

	elif thisTrial['condition']=='congruent' and thisTrial['stim']=='X':
		rightStimText = thisTrial['stim']
		leftStimText = ''
		ans = 'm'
	elif thisTrial['condition']=='congruent' and thisTrial['stim']=='0':
		leftStimText = thisTrial['stim']
		rightStimText = ''
		ans = 'z'
elif expInfo['counterbalance']=='1':
	bindings = {'X':'z', 'O':'m'}
	if thisTrial['condition']=='incongruent' and thisTrial['stim']=='X':
		rightStimText = thisTrial['stim']
		leftStimText = ''
		ans = 'z'
	elif thisTrial['condition']=='incongruent' and thisTrial['stim']=='0':
		leftStimText = thisTrial['stim']
		rightStimText = ''
		ans = 'm'

	elif thisTrial['condition']=='congruent' and thisTrial['stim']=='X':
		leftStimText = thisTrial['stim']
		rightStimText = ''
		ans = 'z'
	elif thisTrial['condition']=='congruent' and thisTrial['stim']=='0':
		rightStimText = thisTrial['stim']
		leftStimText = ''
		ans = 'm'