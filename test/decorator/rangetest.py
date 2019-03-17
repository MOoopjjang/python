#!python
#-*- coding:utf-8 -*-


trace = True

def rangetest(**argchecks):
	def onDecorator(func):
		if not __debug__:
			return func
		else:
			code = func.__code__
			allargs = code.co_varnames[:code.co_argcount]
			funcname = func.__name__
			def onCall(*pargs , **kargs):
				# 모든 parg는 위치에 의해 첫 N개의 인수에 매칭시킴
				# 나머지는 karg에 있거나 , 생략된 기본값
				expected = list(allargs)
				positionals = expected[:len(pargs)]

				for(argname , (low , high)) in argchecks.items():
					# 검사할 모든 args에 대해
					if argname in kargs:
						#이름에 의해 전달됨
						if kargs[argname] < low or kargs[argname] > high:
							errmsg = '{0} argument "{1}" not in {2}..{3}'
							errmsg = errmsg.format(funcname , argname , low , high)
							raise TypeError(errmsg)
					elif argname in positionals:
						# 위치에 의해 전달됨
						position = positionals.index(argname)
						if pargs[position] < low or pargs[position] > high:
							errmsg = '{0} argument "{1}" not in {2}..{3}'
							errmsg = errmsg.format(funcname , argname , low , high)
							raise TypeError(errmsg)
					else:
						#전달되지 않은 인수는 기본값으로 가정
						if trace:
							print('Argument "{0}" defaulted'.format(argname))

				return func(*pargs , **kargs)
			return onCall
	return onDecorator