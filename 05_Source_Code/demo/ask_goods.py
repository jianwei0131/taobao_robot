# -*- coding: utf-8 -*-
import top.api

req=top.api.TbkItemInfoGetRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.num_iids="123,456"
req.platform=1
req.ip="11.22.33.43"
try:
	resp= req.getResponse()
	print(resp)
except Exception as e:
	print(e)