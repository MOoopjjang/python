#!python3
#-*- coding:utf-8 -*-


"""
  089 : 빌보드 차트 웹사이트에서 정보 읽어오기 ( 빌보드 차트 웹사이트 (https://www.billboard.com/charts/hot-100/)) -OK
  090 : 빌보드 차트 웹사이트에서 정보를 읽어 리스트에 저장하기 
        빌보트 차트 웹사이트 ( https://www.billboard.com)에서 빌보드 정보를 읽어서 리스트에 저장해 보자 -OK
  091 : 이번주 빌도브 차트 기준 날짜찾기
         이번주 빌보드 차트의 기준 날짜를 찾아보자.
  092 : 찾으려는 날짜의 빌보드 차트를 리스트에 저장하기
  		찾으려는 날짜의 빌보드 차트 내용을 읽어 리스트에 저장해 보자.
  093 : 이번주 빌보드 차트를 파싱하여 객체로 저장하기
  		이번주 빌보드 차트를 파싱하여 객체로 저장
  094 : 빌보드 차트 정보를 csv로 저장하고 읽기
  095 : 빌보드 차트 정보를 json으로 저장하고 읽기		 - Ok		             
"""


import requests
import bs4


from result_file_write_decorator import rfwd

class BillBoardManager:
	def __init__( self  , _url ):
		self._url = _url
		self._html = None
		

	def requestInfo( self ):
		res = requests.get( self._url , timeout = 3)
		res.raise_for_status()
		self._html = res.text


	@rfwd(mode = True)
	def parsing( self ):
		bsObj = bs4.BeautifulSoup(self._html , 'html.parser')
		elm = bsObj.find('div' , {'class':'container chart-container container--xxlight-grey container--no-side-padding'})
		elm1 = elm.find('div' , {'class':'chart-details '})
		chartElm = elm1.findAll('div' , {'class':'chart-list-item'})
		print(len(chartElm))

		bbm = {}
		for chart in chartElm:
			m = { key:chart.attrs[key] for key in chart.attrs if key.startswith('data-') }
			bbm[chart.attrs['data-rank']] = m

		return bbm


	def loadData( self , _path ):
		import json
		with open(_path , 'r') as fr:
			jObj = json.load(fr)
		return jObj
			





def main():
	bbm = BillBoardManager('https://www.billboard.com/charts/hot-100/')
	bbm.requestInfo()
	bbm.parsing()
	bbm.loadData('billboard.json')
	


if __name__ == '__main__':
	main()



