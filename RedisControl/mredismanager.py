#!python
#coding:utf-8

# Makey By MOoop
# Desc
# 	Redis 서버간에 compare , copy , delete등의 작업을 한다
# History
#	- 2018.04.30 Create	
#	- 2018.05.04 setKey() 메소드 추


import os , sys
import datetime

from mcommmodule import getLogger , getCurrentDefTime


from multiprocessing import Process
import redis
from rediscluster import RedisCluster
from rediscluster import StrictRedisCluster


class MRedisManager():
	divideCount = 100000
	nProcessCount = 50

	def __init__(self , _config):

		# reload(sys)
		# sys.setdefaultencoding("ISO-8859-1")

		self.__configObj = _config
		self.__confDict = self.__configObj.getConfigInfo()
		self.__type = 'rtor'
		self.__mode = 'compare'
		self.__srcr = None
		self.__tgtr = None
		self.__bSet = False
		self.__key = None
		self.__fieldKey = None


	def __string_get__(self , _key , _r):
		v = _r.get(_key)
		if v != None:
			return v
		return None

	def __hash_get__(self , _key , _hashkey , _r):
		v = _r.hget(_key , _hashkey)	
		if v != None:
			return v
		return None


	#	
	# Desc	
	# 	- Hash type SRC redis값을 TARGET redis에서 copy한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.9
	#
	def __s_comp__(self , _key):
		src_v = self.__string_get__(_key , self.__srcr)
		tgt_v = self.__string_get__(_key , self.__tgtr)

		result = None
		if src_v == None or tgt_v == None:
			result = 'diff'
		elif src_v != tgt_v:
			result = 'diff'
		else:
			result = 'same'	
		
		fSameName = os.getcwd()+'/'+str(os.getpid())+'_same.txt'
		fErrorName = os.getcwd()+'/'+str(os.getpid())+'_error.txt'
		fName = fSameName
		if result == 'diff':fName = fErrorName
		fw = open(fName , 'a') if os.path.exists(fName) else fw = open(fName , 'w')

		# fw = None
		# if os.path.exists(fName) == True:
		# 	fw = open(fName , 'a')
		# else:
		# 	fw = open(fName , 'w')

		fw.write('key:{}-{}}'.format(_key,result))
		# fw.write('key:%s-%s'%(_key,result))
		fw.close()	



	#	
	# Desc	
	# 	- Hash type SRC redis값을 TARGET redis에서 copy한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.9
	#
	def __h_comp__(self , _key , _key_list , from_r , to_r):
		count = 0
		getLogger().info('--pid:{}-- compare start'.format(os.getpid()))
		error_log = []
		same_log = []
		for fkey in _key_list:
			# From GET
			src_v = self.__hash_get__(_key , fkey , from_r)
			tgt_v = self.__hash_get__(_key , fkey , to_r)

			if src_v == None or tgt_v == None:
				error_log.append(('%s:%s is diff'%(_key , fkey)))
				continue

			if 	src_v != tgt_v:
				error_log.append(('%s:%s is diff'%(_key , fkey)))
				continue

			same_log.append(('%s:%s is same'%(_key , fkey)))
			
			# Couting...
			count+=1
			if count % 100000 == 0:
				getLogger().info('--pid:{}-- compare count:{}'.format(os.getpid(), count))

		getLogger().info('--pid:{}-- compare end'.format(os.getpid()))

		# Error log Write
		if len(error_log) > 0:
			getLogger().info('--pid:{}-- error log Creating...'.format(os.getpid()))
			errWrite = open(os.getcwd()+'/'+str(os.getpid())+'_error.txt' , 'w')
			for err in error_log:
				errWrite.write(err.strip()+'\n')
			errWrite.close()
			error_log[:]
			getLogger().info('--pid:{}-- error log Write Complete...')
		else:
			getLogger().info('--pid:{}--  Not Error'.format(os.getpid()))

		if len(same_log) > 0:
			getLogger().info('--pid:{}-- same_log log Creating...'.format(os.getpid()))
			sameWrite = open(os.getcwd()+'/'+str(os.getpid())+'_same.txt' , 'w')
			for same in same_log:
				sameWrite.write(same.strip()+'\n')
			sameWrite.close()
			same[:]
			getLogger().info('--pid:{}-- same log Write Complete...')
		
		


	#	
	# Desc	
	# 	- Hash type SRC redis값을 TARGET redis에서 copy한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.9
	#
	def __h_insert__(self , _key , _key_list , from_r , to_r):
		count = 0
		getLogger().info('--pid:{}-- inseart start'.format(os.getpid()))
		error_log = []
		for fkey in _key_list:
			# From GET
			v = self.__hash_get__(_key , fkey , from_r)
			if v == None:
				error_log.append(('%s:%s is error'%(_key , fkey)))
				continue

			# To Set
			to_r.hset(_key , fkey , v)
			
			# Couting...
			count+=1
			if count%100000 == 0:
				getLogger().info('--pid:{}-- insert count'.format(count))

		getLogger().info('--pid:{}-- insert end'.format(os.getpid()))

		# Error log Write
		if len(error_log) > 0:
			getLogger().info('--pid:{}-- error log Creating...'.format(os.getpid()))
			errWrite = open(os.getcwd()+'/'+str(os.getpid())+'_error.txt' , 'w')
			for err in error_log:
				fw.write(err.strip()+'\n')
			fw.close()
			error_log[:]
			getLogger().info('--pid:{}-- error log Write Complete...')
		else:
			getLogger().info('--pid:{}--  Not Error'.format(os.getpid()))


	#	
	# Desc	
	# 	- target redis에 key값에 해당되는 필드 삭제
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.9
	#
	def __key_delete__(self , _key):
		self.__tgtr.delete(_key)



	#	
	# Desc	벼
	# 	- String type SRC redis값을 TARGET redis에서 copy한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.6
	#
	def __copy_string__(self , _key):
		v = self.__string_get__(_key , self.__srcr)
		if v != None:
			getLogger().info('set key:{} , v:{}'.format(_key , v))
			self.__tgtr.set(_key ,v)


	#	
	# Desc	
	# 	- String type SRC redis값을 TARGET redis에서 copy한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.6
	#
	def __string__(self , _key):
		if self.__mode == 'copy':
			self.__copy_string__(_key)
		elif self.__mode == 'compare':
			self.__s_comp__(_key)
		elif self.__mode == 'delete':
			self.__key_delete__(_key)
		else:
			pass


	#	
	# Desc	
	# 	- String type SRC redis값을 TARGET redis에서 copy한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.6
	#
	def __hashmap__(self , _key , _fkey = None):
		keyLen = int(self.__srcr.hlen(_key)) if _fkey == None else 1
		keys = self.__srcr.hkeys(_key) if _fkey == None else list(_fkey)

		getLogger().info('----hash  key:{} , size:{} ----'.format(_key , keyLen))

		procs = []

		try:
			# Mode Select ( copy , compare )
			cur_func = None
			if self.__mode == 'copy':
				cur_func = self.__h_insert__
			elif self.__mode == 'compare':
				cur_func = self.__h_comp__
			elif self.__mode == 'delete':
				cur_func = self.__key_delete__
			else:
				raise Exception('unknown Mode : {}'.format(self.__mode))

			if self.__mode == 'delete':
				cur_func(_key)
			else:
				if keyLen >= MRedisManager.divideCount:  #MP
					bit = int(keyLen / MRedisManager.nProcessCount)
					index = 0
					for index in range(0 , MRedisManager.nProcessCount):
						start = int(index*bit)
						end = int(start+bit)
						getLogger().debug('--i:{} , s:{} , e:{}  , d :{} --'.format(index , start , end , end-keyLen))
						if index == (MRedisManager.nProcessCount -1):
							end = keyLen
						getLogger().debug('--i:{} , s:{} , e:{} , t:{} --'.format(index , start , end , keyLen))
						p = Process(target = cur_func , args = (_key , keys[start:end] , self.__srcr , self.__tgtr ))
						procs.append(p)
						p.start()


					#JOINing...
					for proc in procs:
						proc.join()
				else: # No MP
					cur_func(_key , keys , self.__srcr , self.__tgtr)

		except KeyboardInterrupt:
			for proc in procs:
				proc.terminate()


	#	
	# Desc	
	# 	- Key값이 많을 경우 Multi Processing...
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.6
	#
	def __m_key_proc__(self , _keys , _size):
		procs = []

		try:
			bit = int(_size / MRedisManager.nProcessCount)
			for index in range(0 , MRedisManager.nProcessCount):
				start  = index * bit
				end = start + bit
				if index == (MRedisManager.nProcessCount -1):
					end = _size
				p = Process(target = self.__key_proc__ , args = (_keys[start:end] , _size))
				procs.append(p)
				p.start()

			for proc in procs:
				proc.join()
		except KeyboardInterrupt:
			for proc in procs:
				proc.terminate()

		


	#	
	# Desc	
	# 	- 
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.6
	#
	def __key_proc__(self , _keys , _size):
		for key in _keys:
			if self.__srcr.type(key) == 'string' or self.__tgtr.type(key) == 'string':
				self.__string__(key)
			elif self.__srcr.type(key) == 'hash' or self.__tgtr.type(key) == 'hash':
				self.__hashmap__(key , self.__fieldKey)
			else:
				getLogger().info('지원하지 않는 type입니다.-- {}'.format(self.__srcr.type(key)))


	#	
	# Desc	
	# 	- .
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.6
	#
	def __compare__(self):
		pass



	#	
	# Desc	
	# 	- src , target Redis Connection을 설정한다.
	#
	# Method Type:
	#	PRIVATE
	#   
	# return X
	#
	# version 0.5
	#
	def __connectionRedisServer__(self):
		# Redis Connection
		if self.__type == 'rtoc':
			srcHost = self.__confDict['srchosts']['host0']['host']
			srcPort = self.__confDict['srchosts']['host0']['port']
			srcPwd = None
			if self.__confDict['srcpwd'] != None and len(self.__confDict['srcpwd']) > 0:
				srcPwd = self.__confDict['srcpwd']

			self.__srcr = redis.StrictRedis( srcHost , port = srcPort , charset='utf-8' , db = 0 , password = srcPwd)	

			startup_nodes = []
			tgt_hosts_dict = self.__confDict['tgthosts']
			getLogger().debug('keys ::{}'.format(tgt_hosts_dict.keys()))
			for key in tgt_hosts_dict.keys():
				d = {}
				d['host'] = tgt_hosts_dict[key]['host']
				d['port'] = int(tgt_hosts_dict[key]['port'])
				startup_nodes.append(d)

			getLogger().debug('startup_nodes:{}'.format(startup_nodes))
			self.__tgtr = StrictRedisCluster(startup_nodes = startup_nodes , decode_responses = False)
		elif self.__type == 'rtor':
			# Source Redis
			srcHost = self.__confDict['srchosts']['host0']['host']
			srcPort = self.__confDict['srchosts']['host0']['port']
			srcPwd = None
			if self.__confDict['srcpwd'] != None and len(self.__confDict['srcpwd']) > 0:
				srcPwd = self.__confDict['srcpwd']

			self.__srcr = redis.StrictRedis( srcHost , port = srcPort , db = 0 , password = srcPwd)	

			# Target Redis
			tgtHost = self.__confDict['tgthosts']['host0']['host']
			tgtPort = self.__confDict['tgthosts']['host0']['port']
			tgtPwd = None
			if self.__confDict['tgtpwd'] != None and len(self.__confDict['tgtpwd']) > 0:
				tgtPwd = self.__confDict['tgtpwd']

			self.__tgtr = redis.StrictRedis( tgtHost , port = tgtPort , db = 0 , password = tgtPwd)	

		elif self.__type == 'rtorp':
			pass
		else:
			pass



	#	
	# Desc	
	# 	- redis type 및 진행할 job 셋팅
	#	- redis Connection을 설정한단
	#
	# Method Type:
	#	PUBLIC
	#   
	# return X
	#
	# version 0.9
	#
	def setTypeMode(self , _type , _job):
		if self.__confDict == None:
			raise Exception('Config is Null')

		getLogger().debug(type(self.__confDict))
		if _type not in self.__confDict['types']:
			raise Exception('support type ::'+str(self.__confDict['types']))

		if _job not in self.__confDict['jobmodes']:
			raise Exception('support job ::'+str(self.__confDict['jobmodes']))

		self.__type = _type
		self.__mode = _job
		self.__bSet = True

		self.__connectionRedisServer__()
		return self


    #	
	# Desc	
	# 	- Redis Key 값과  hash의 경우 field key값까지 설정할수 있다
	#
	# Method Type:
	#	PUBLIC
	#   
	# return X
	#
	# version 0.9
	#
	def setKey(self , _key = None , _fieldKey = None):
		self.__key = _key
		self.__fieldKey = _fieldKey
		return self



	#	
	# Desc	
	# 	- 요청한 REDIS작업을 실행하는 MAIN API
	#
	# Method Type:
	#	PUBLIC
	#   
	# return X
	#
	# version 0.6
	#
	def run(self):
		if self.__bSet == False:
			raise Exception('setTypeMode Method not Called!!')

		getLogger().info('-- Start time :{}'.format(getCurrentDefTime()))


		if self.__srcr == None or self.__tgtr == None:
			raise Exception('Redis Not Connection...')


		if self.__key != None:
			self.__key_proc__([self.__key] , 1)
		else:
			srcDbSize = self.__srcr.dbsize()
			srcKeys = self.__srcr.keys()
			getLogger().info('-- src key size:{}'.format(srcDbSize))
			if srcDbSize > MRedisManager.divideCount:  # MP
				self.__m_key_proc__(srcKeys , srcDbSize)
			else:
				self.__key_proc__(srcKeys , srcDbSize)

		getLogger().info('-- End time :{}'.format(getCurrentDefTime()))



	def init(self):
		pass	
