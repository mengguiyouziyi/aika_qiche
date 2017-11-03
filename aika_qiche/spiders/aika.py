# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
from scrapy.selector import Selector
from random import choice
from aika_qiche.items import AikaQicheItem


class TouzishijianSpider(scrapy.Spider):
	# ?type=1&page=182
	name = 'aika'
	burl = 'http://dealer.xcar.com.cn/d1000/{}.htm'
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			'upgrade-insecure-requests': "1",
			# 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://dealer.xcar.com.cn/",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			# 'cookie': "_fwck_dealer=05698dcfab4d0a3d05cffa0533bf38ba; _appuv_dealer=694a8660657863eeae27cbab42b7070a; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc1c5aa9119; _fwck_www=1c6576ba7f6f7cef10003c5235601bf0; _appuv_www=5a4924c5f3678bc5d84ddb85950e6e69; _Xdwuv=59f97576be53e; _fwck_tools=beff19be34a55210362a18a4564288e1; _appuv_tools=c2eb9719173cfe9717cd95acfce8456a; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509695363; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509694555; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509695363",
			'cache-control': "no-cache",
			'postman-token': "80cfe883-c0d9-1cd0-39a6-47410b7a679c"
		}
	}
	# cookies = ['_fwck_dealer=05698dcfab4d0a3d05cffa0533bf38ba; _appuv_dealer=694a8660657863eeae27cbab42b7070a; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc1c5aa9119; _fwck_www=1c6576ba7f6f7cef10003c5235601bf0; _appuv_www=5a4924c5f3678bc5d84ddb85950e6e69; _Xdwuv=59f97576be53e; _fwck_tools=beff19be34a55210362a18a4564288e1; _appuv_tools=c2eb9719173cfe9717cd95acfce8456a; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509695363; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509694555; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509695363',
	cookies = [
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641; _fwck_dealer=6ea5ed99d5c45bd8555072121dbb0f4b; _appuv_dealer=6dec38978e23b3e445a967c75e4b14ad; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000; ad__city=475; _Xdwnewuv=1; _Xdwstime=1509704670; uv_firstv_refers=; _fwck_tools=b1a57b455c47d18271f691e9ffbd9785; _appuv_tools=adf526b44036f26458329ac304c8b7e7; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _fwck_www=82c1b742edf4927d83f70119645dd26b; _appuv_www=2f5ced45baa341178b3f66ebbb24ef1c; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509704671',
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641,1509704835; _fwck_dealer=6ea5ed99d5c45bd8555072121dbb0f4b; _appuv_dealer=6dec38978e23b3e445a967c75e4b14ad; ad__city=475; _Xdwnewuv=1; _Xdwstime=1509704839; uv_firstv_refers=http%3A//dealer.xcar.com.cn/d1000/13.htm%3Ftype%3D2; _fwck_tools=b1a57b455c47d18271f691e9ffbd9785; _appuv_tools=adf526b44036f26458329ac304c8b7e7; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _fwck_www=82c1b742edf4927d83f70119645dd26b; _appuv_www=2f5ced45baa341178b3f66ebbb24ef1c; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509704841',
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641,1509704835; _fwck_dealer=6ea5ed99d5c45bd8555072121dbb0f4b; _appuv_dealer=6dec38978e23b3e445a967c75e4b14ad; ad__city=475; _Xdwnewuv=1; _Xdwstime=1509704855; uv_firstv_refers=http%3A//dealer.xcar.com.cn/d1000/13.htm%3Ftype%3D2; _fwck_tools=b1a57b455c47d18271f691e9ffbd9785; _appuv_tools=adf526b44036f26458329ac304c8b7e7; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _fwck_www=82c1b742edf4927d83f70119645dd26b; _appuv_www=2f5ced45baa341178b3f66ebbb24ef1c; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509704856'
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; _Xdwstime=1509705844; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509705982; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509705982 ',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706043; uv_firstv_refers=; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706350; uv_firstv_refers=; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706351',
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641,1509704835; _fwck_dealer=6ea5ed99d5c45bd8555072121dbb0f4b; _appuv_dealer=6dec38978e23b3e445a967c75e4b14ad; ad__city=475; _Xdwnewuv=1; _Xdwstime=1509704932; uv_firstv_refers=http%3A//dealer.xcar.com.cn/d1000/13.htm%3Ftype%3D2; _fwck_tools=b1a57b455c47d18271f691e9ffbd9785; _appuv_tools=adf526b44036f26458329ac304c8b7e7; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _fwck_www=82c1b742edf4927d83f70119645dd26b; _appuv_www=2f5ced45baa341178b3f66ebbb24ef1c; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509704932',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706463; uv_firstv_refers=http%3A//dealer.xcar.com.cn/35283/; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706465',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706422; uv_firstv_refers=http%3A//dealer.xcar.com.cn/35283/; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706422',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706536; uv_firstv_refers=http%3A//dealer.xcar.com.cn/35283/; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706536; PHPSESSID=d8nn96du4kloo32pvqahgpfkn2',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706588; uv_firstv_refers=http%3A//dealer.xcar.com.cn/35283/; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706589; PHPSESSID=d8nn96du4kloo32pvqahgpfkn2',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509705992; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509705993',
		'_Xdwuv=5097060430749; _fwck_dealer=6d0e3a1e715ab2963e7b4067e25031a6; _appuv_dealer=3030c8ed9e42dfb60b3bf4e0310c8ad6; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509706502; uv_firstv_refers=http%3A//dealer.xcar.com.cn/35283/; _PVXuv=59fc493cbc639; _fwck_www=dc28c70ad3d8c82d168c978477ecb7bc; _appuv_www=ab5c2ecb6efcd68989ad27a4c320be8f; _fwck_tools=ba7b927b5d62431e43e849713c270cf4; _appuv_tools=827b0e924ab034feef26865959dd62ce; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509706045; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706502',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509706643; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509706643',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509707012; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509707012',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509707059; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509707059',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509707104; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509707105',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509707218; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509707218',
		'_fwck_dealer=c48a6e1875096ee34b3a6dc19a993e87; _appuv_dealer=90a929ca3952c8393c4b3d90c3caaf94; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; ad__city=475; _Xdwnewuv=1; uv_firstv_refers=http%3A//dealer.xcar.com.cn/; _PVXuv=59fc48746d47f; _fwck_www=f7f94fc926631aa0b6d26d0e05e39af1; _appuv_www=032628515153846c0c21eeb9e3667f67; _Xdwuv=5097058441432; _fwck_tools=59d30062ccacb15f927f521e657d0384; _appuv_tools=622539ac1e1bbc7e7d09ae2f9aa1413c; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _Xdwstime=1509707367; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509705845; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509707367',
		'_fwck_dealer=3e2309f58fe68f5140f7a65c75304266; _appuv_dealer=1b60d7fccda5169cc6a5c837b64e05ee; BIGipServerpool-c26-xcar-dealerweb1-80=1221136138.20480.0000; ad__city=475; _Xdwnewuv=1; _Xdwstime=1509709041; uv_firstv_refers=http%3A//dealer.xcar.com.cn/d1000/20.htm%3Ftype%3D1%26page%3D9; _PVXuv=59fc54f186f94; _fwck_www=e83c2661933187394aa6936c31b0b3c0; _appuv_www=b949990b998861fec4aab12ac4f90601; _Xdwuv=5097090414135; _fwck_tools=c53f7d319911ce03e40e0fdd168144a3; _appuv_tools=75edc124f1c31468c9950f8ec4168794; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509709042; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509709042',
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641,1509704835; _fwck_dealer=6ea5ed99d5c45bd8555072121dbb0f4b; _appuv_dealer=6dec38978e23b3e445a967c75e4b14ad; ad__city=475; _Xdwnewuv=1; _fwck_tools=b1a57b455c47d18271f691e9ffbd9785; _appuv_tools=adf526b44036f26458329ac304c8b7e7; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; _fwck_www=82c1b742edf4927d83f70119645dd26b; _appuv_www=2f5ced45baa341178b3f66ebbb24ef1c; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509709124; CAR_HiddenCompare=101a100a105a72; _Xdwstime=1509709124; uv_firstv_refers=http%3A//newcar.xcar.com.cn/car/9-0-0-0-0-0-0-0-0-0-0-0/',
		'_Xdwuv=5097092427708; _fwck_dealer=4eb191b8c11cc5a28a728372b73857d6; _appuv_dealer=075c6af01f2c06ceaf27a5029988bd22; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000',
		'_fwck_dealer=79628f2ac86335659bd37746c19cc3f7; _appuv_dealer=cdd1e592c0d88135fda788ade4d49f49; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509709298; uv_firstv_refers=http%3A//dealer.xcar.com.cn/115975/; _PVXuv=59fc55f2423f8; _fwck_www=95f96dac9bc4276dca79ac81ab9383e9; _appuv_www=c7ca700bad750ac45b35952b99060833; _Xdwuv=5097092983649; _fwck_tools=2c21bdcefcc8f11d55dfa4f862a0ece4; _appuv_tools=ebb77eb3d7d453ae0a9bd674d0046a40; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509709299; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509709299; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D',
		'_fwck_dealer=0bed659bffa1573a9d1c5356c4de5592; _appuv_dealer=bf1d27e301939a3f2a18e857c92e686d; BIGipServerpool-c26-xcar-dealerweb1-80=1204358922.20480.0000; _Xdwnewuv=1; _Xdwstime=1509709361; uv_firstv_refers=http%3A//dealer.xcar.com.cn/35157/; _PVXuv=59fc563194645; _fwck_www=7e700d4e711f991a102c69e53eefa1f9; _appuv_www=a6f4ba2b581b4752a858d662be7478a3; _Xdwuv=5097093605745; _fwck_tools=4a58edbace3341f2b49ab74a73d1cc86; _appuv_tools=bec0505dd8c7e6be90d988ca30c21d10; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509709361; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=1509709361; _locationInfo_=%7Burl%3A%22h%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D',
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641,1509704835; _fwck_dealer=88b12f311fbcfc2b412b6201a9c5c08a; _appuv_dealer=10f0fb9d9e1621e6167d5a36d6b2df2b; BIGipServerpool-c26-xcar-dealerweb1-80=1221136138.20480.0000',
		'_Xdwuv=599c041b985b1; _PVXuv=599c041b0596f; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1509704641,1509704835,1509709514; _fwck_dealer=99a7b9b6446304bd8612304f23cc7eb1; _appuv_dealer=459b23ff0e811cc5f3b4f775803f29d0; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000',
	]
	cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))

	# def start_requests(self):
	# 	start_url = "http://dealer.xcar.com.cn/113220/about.htm"
	# 	yield scrapy.Request(start_url, cookies=self.cookie_dict)
	#
	# def parse(self, response):
	# 	select = Selector(text=response.text)
	# 	intro_list = select.xpath('//div[@class="company_txt"]//text()').extract()
	# 	intro = ''.join([i.strip() for i in intro_list if i]) if intro_list else ''
	# 	short = select.xpath('//div[@class="shop_rh"]/div[@class="store"]/span/text()').extract_first()
	# 	dl_tags = select.xpath('//dl[@class="clearfix"]')
	# 	jibie = ''
	# 	for dl in dl_tags:
	# 		if dl.xpath('./dt/text()').extract_first() != '级别：':
	# 			continue
	# 		jibie = dl.xpath('./dd/text()').extract_first()
	# 		print(jibie)

	def start_requests(self):
		start_url = "http://dealer.xcar.com.cn/"
		yield scrapy.Request(start_url, cookies=self.cookie_dict)

	def parse(self, response):
		select = Selector(text=response.text)
		a_tags = select.xpath('//div[@class="ulcon"]/a')
		for a in a_tags:
			item = AikaQicheItem()
			cat = a.xpath('./text()').extract_first()
			cat_url = a.xpath('./@href').extract_first()
			id = re.search(r'(\d+)\.htm', cat_url).group(1)
			item['cat'] = cat
			# print('type_1', self.burl.format(id))
			yield scrapy.Request(self.burl.format(id), callback=self.parse_list_a, meta={'item': item})
			# print('type_2', self.burl.format(id) + '?type=2')
			yield scrapy.Request(self.burl.format(id) + '?type=2', callback=self.parse_list_b, meta={'item': item})

	def parse_list_a(self, response):
		item = response.meta.get('item')
		select = Selector(text=response.text)
		dl_tags = select.xpath('//div[@id="dlists_4s_isfee"]/ul[@class="dlists_list"]/li/dl')
		# print(len(dl_tags))
		for dl in dl_tags:
			dt_tag = dl.xpath('./dt/a')
			comp_name = dt_tag.xpath('./text()').extract_first()
			comp_url = dt_tag.xpath('./@href').extract_first()
			comp_url = urljoin(response.url, comp_url) + 'about.htm'
			phone = dl.xpath('./dd[@class="phone"]/em/b/text()').extract_first()
			addr = dl.xpath('./dd[@class="site"]/span[2]/text()').extract_first()
			item['comp_name'] = comp_name
			item['comp_url'] = comp_url
			item['phone'] = phone
			item['addr'] = addr
			# print('type_1_comp_url', comp_url)
			yield scrapy.Request(comp_url, callback=self.parse_detail, meta={'item': item})
		p_next = select.xpath('//div[@id="dlists_4s_isfee"]//a[@class="page_down"]/@href').extract_first()
		if not p_next:
			return
		p_next = urljoin(response.url, p_next)
		# print('type_1_next', p_next)
		yield scrapy.Request(p_next, callback=self.parse_list_a, meta={'item': item})

	def parse_list_b(self, response):
		item = response.meta.get('item')
		select = Selector(text=response.text)
		dl_tags = select.xpath('//div[@id="dlists_zh"]/ul[@class="dlists_list"]/li/dl')
		# print(len(dl_tags))
		for dl in dl_tags:
			dt_tag = dl.xpath('./dt/a')
			comp_name = dt_tag.xpath('./text()').extract_first()
			comp_url = dt_tag.xpath('./@href').extract_first()
			comp_url = urljoin(response.url, comp_url) + 'about.htm'
			phone = dl.xpath('./dd[@class="phone"]/em/b/text()').extract_first()
			addr = dl.xpath('./dd[@class="site"]/span[2]/text()').extract_first()
			item['comp_name'] = comp_name
			item['comp_url'] = comp_url
			item['phone'] = phone
			item['addr'] = addr
			# print('type_2_comp_url', comp_url)
			yield scrapy.Request(comp_url, callback=self.parse_detail, meta={'item': item})
		p_next = select.xpath('//div[@id="dlists_zh"]//a[@class="page_down"]/@href').extract_first()
		if not p_next:
			return
		p_next = urljoin(response.url, p_next)
		# print('type_2_next', p_next)
		yield scrapy.Request(p_next, callback=self.parse_list_b, meta={'item': item})

	def parse_detail(self, response):
		item = response.meta.get('item')
		select = Selector(text=response.text)
		intro_list = select.xpath('//div[@class="company_txt"]//text()').extract()
		intro = ''.join([i.strip() for i in intro_list if i]) if intro_list else ''
		short = select.xpath('//div[@class="shop_rh"]/div[@class="store"]/span/text()').extract_first()
		dl_tags = select.xpath('//dl[@class="clearfix"]')
		jibie = ''
		phone = item['phone']
		addr = item['addr']
		for dl in dl_tags:
			text = dl.xpath('./dt/text()').extract_first()
			if text == '级别：':
				jibie = dl.xpath('./dd/text()').extract_first()
			elif text == '电话：':
				phone = dl.xpath('./dd/em/text()').extract_first()
			elif text == '地址：':
				addr = dl.xpath('./dd/p/text()').extract_first()
			else:
				continue
		item['intro'] = intro
		item['short'] = short
		item['jibie'] = jibie
		item['phone'] = phone
		item['addr'] = addr
		yield item
