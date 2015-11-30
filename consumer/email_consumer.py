#!/usr/bin/env python
# coding=utf-8
import logging, time, collections
from kafka import KafkaConsumer
import sendmail

#kafka consumer client
def main():
    # more advanced consumer -- multiple topics w/ auto commit offset
    # management
    consumer = KafkaConsumer('email',  bootstrap_servers=['localhost:9092'], group_id='None', auto_commit_enable=True, auto_commit_interval_ms=30 * 1000, auto_offset_reset='smallest')
    
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
            print ("email eval msg is %s")  % (str(msg.keys()))
        except:
            print ("email error msg is %s")  % (m)
        """
        import json
        msg = json.loads(m.value)
        print('json msg is %s' % (str(msg)))
        print
        """
        #format mail info entry
        mailParam = formatEmailEntry(msg)
        #send mail entry info 
        sendMail(mailParam)
        #end send mail
        #end format
        consumer.task_done(m)
        # If auto_commit_enable is False, remember to commit() periodically
        consumer.commit()
    
    # Batch process interface
    while True:
        for m in kafka.fetch_messages():
            # process_message(m)
            consumer.task_done(m)
        time.sleep(1)
            
#format sended mail info entry from template            
def formatEmailEntry(msg):
    pass
    mailparam = {}
    mailparam['fro'] = 'wei.yun@zhiguoguo.com'
    mailparam['to'] = ['pengdi.yang@zhiguoguo.com','yangpengdi2008@163.com']
    mailparam['to'] = ['pengdi.yang@zhiguoguo.com']
    mailparam['pwd'] = 'zg123456'
    mailparam['subject'] = 'test'
    mailparam['text'] = 'htmlstr'
    mailparam['text'] = msg['body']
    mailparam['files'] = ['jobsched.cfg']
    mailparam['files'] = []
    mailparam['server'] = 'smtp.exmail.qq.com'
    mailparam['server_port'] = 25
    mailparam['entry'] = 'this is context'
    
    return mailparam
    

#发送邮件函数
def sendMail(mailparam):
    try:
        #put mail job into send mail process
        mail = sendmail.SendmailJob(mailparam)
        
        sendstatus = mail.__call__('dfdkfjd')
        if sendstatus :
            print('sucess to send mail to %s' % (str(mailparam)))
            try:
                print('sucess to send mail to %s mail title is %s'  % (mailparam["entry"]['to'] , mailparam["entry"]["subject"] ))
            except:
                pass
        else:
            print('error to send mail to %s ' % (mailparam["entry"]['to']))
        del mail
    except:
        del mail
        print('error to send mail to %s ' % (str(mailparam)))
    
    
    #end put mail 
        

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()