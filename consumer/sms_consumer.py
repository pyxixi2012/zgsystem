#!/usr/bin/env python
# coding=utf-8
import logging, time, collections
from kafka import KafkaConsumer
import httplib
import re
import urllib ,urllib2


"""
* 方法名称：getMD5
* 功    能：字符串MD5加密
* 参    数：待转换字符串
* 返 回 值：加密之后字符串
"""
def getMD5(sourceStr):
    import hashlib
    """
    Return the md5 hash of the password+salt
    """
    return hashlib.md5(sourceStr).hexdigest().upper()

#kafka consumer client
def main():
    # more advanced consumer -- multiple topics w/ auto commit offset
    # management
    consumer = KafkaConsumer('sms',  bootstrap_servers=['localhost:9092'], group_id='None', auto_commit_enable=True, auto_commit_interval_ms=30 * 1000, auto_offset_reset='smallest')

    # Infinite iteration
    for m in consumer:
        # do_some_work(m)

        # Mark this message as fully consumed
        # so it can be included in the next commit
        #
        # **messages that are not marked w/ task_done currently do not commit!
        #print 'm is ',m
        #post data example is ,{"body":{"aa":["1","2",3]}}

        try:
            msg = eval(m.value)
            print ("sms eval msg is %s")  % (str(msg.keys()))
        except:
            print ("sms error msg is %s")  % (m)

        """

        import json
        msg = json.loads(m.value)
        print 'json msg is ',msg
        """

        consumer.task_done(m)

        # If auto_commit_enable is False, remember to commit() periodically
        consumer.commit()

    # Batch process interface
    while True:
        for m in kafka.fetch_messages():
            # process_message(m)
            consumer.task_done(m)

"""
 * 短信发送
 *
 * @param content 如：测试短信【知果果网】
 * @param tel
 * @return 1:成功  0：失败
"""
def sendMsg(content, tel):
    status = 0
    #短信发送
    #发送信息 失败重复三次
    result_mt = mdsmssend(tel, content, "", "", "", "")
    if result_mt == "":
        mdsmssend(tel, content, "", "", "", "")
    if result_mt == "":
        mdsmssend(tel, content, "", "", "", "")

    if result_mt == "":
        print("信息发送结果：% s " %  (result_mt))
        status = 0
    else:
        print("信息发送结果：% s " %  (result_mt))
        status = 1
    return status

"""
 * 方法名称：mdsmssend
 * 功    能：发送短信
 * 参    数：mobile,content,ext,stime,rrid,msgfmt(手机号，内容，扩展码，定时时间，唯一标识，内容编码)
 * 返 回 值：唯一标识，如果不填写rrid将返回系统生成的
"""
def mdsmssend(mobile, content, ext, stime,rrid, msgfmt):
    pwd = getMD5(sn + password)
    result = ""
    content = urllib.quote(content)
    soapAction = "http://entinfo.cn/mdsmssend"
    xml = '<?xml version="1.0" encoding="utf-8"?>'
    xml += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    xml += "<soap:Body>"
    xml += '<mdsmssend  xmlns="http://entinfo.cn/">'
    xml += "<sn>" + sn + "</sn>"
    xml += "<pwd>" + pwd + "</pwd>"
    xml += "<mobile>" + mobile + "</mobile>"
    xml += "<content>" + content + "</content>"
    xml += "<ext>" + ext + "</ext>"
    xml += "<stime>" + stime + "</stime>"
    xml += "<rrid>" + rrid + "</rrid>"
    xml += "<msgfmt>" + msgfmt + "</msgfmt>"
    xml += "</mdsmssend>"
    xml += "</soap:Body>"
    xml += "</soap:Envelope>"

    print(('soap xml is %s') % (xml))

    print(('connect info is %s ,%s,%s, %d, %s') % (serviceURL ,servicePORT, service, len(xml),soapAction))
    webservice = httplib.HTTP(serviceURL,servicePORT)
    webservice.putrequest("POST", service)
    webservice.putheader("Content-type", "text/xml; charset=gb2312")
    webservice.putheader("Content-length", "%d" % len(xml))
    webservice.putheader("SOAPAction",soapAction)
    webservice.endheaders()
    webservice.send(xml)

    (status_code, message, reply_headers) = webservice.getreply()
    reply_body = webservice.getfile().read()
    print "status code:", status_code
    print "status message:", message
    print "HTTP reply body:\n", reply_body
    #get send sms Result
    regx = re.compile('<mdsmssendResult>(.*)</mdsmssendResult>')
    return regx.findall(reply_body)[0]

#send sms to webservice gw using http get method
def sendSMST(telNum,sms):
    import urllib ,urllib2
    '''
    发送短信
    '''
    try:
        #smsUrl= config.SMS.SMSURL
        smsUrl ='http://sdk2.entinfo.cn:8061/webservice.asmx'
        md5pwd = getMD5('%s%s'%(sn, password)).upper()
        msg =urllib.quote(sms)
        geturl = '/mdsmssend?sn=%s&pwd=%s&mobile=%s&content=%s&ext=%s&stime=%s&rrid=%s&msgfmt=%s'%(sn,md5pwd,telNum,msg,'','','','')
        get_url =('%s%s'%(smsUrl,geturl))
        req = urllib2.Request(get_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page
    except Exception,e:print e;return None



if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    #main()
    sendMsg("test sms from zhiguoguo 【知果果】", "18611740968")
    #sendSMST("18611740968","test sms from zhiguoguo【知果果】")
