#!python3
#-*- coding:utf-8 -*-



def tag( name , *content , cls = None , **attrs ):
	"""
	하나이상의 HTML tag를 생성한다.
	"""
	print('='*50)
	print('name :%s \n contents : %s \n cls : %s \n attrs : %s \n'%(name , content , cls , attrs))
	print('='*50)

	if cls is not None:
		attrs['class'] = cls

	if attrs:
		attr_str = ' '.join('%s=%s'%(attr , value) for attr , value in sorted(attrs.items()))
	else:
		attr_str = ''

	if content:
		return '\n'.join('<%s %s>%s</%s>'%(name , attr_str , c , name) for c in content)
	else:
		return '<%s%s />'%(name , attr_str)



if __name__ == '__main__':
	t = tag('br')
	print(t)

	t = tag('p' , 'hello')
	print(t)

	t = tag('p' , 'hello' , 'hi')
	print(t)

	t = tag('p' , 'hello' , 'hi' , id=33)
	print(t)

	t = tag('p' , 'hello', cls='sidebar')
	print(t)



