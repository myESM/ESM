import datetime,os,platform
import main as main
import datetime
import time


def run_task(end_time):

    print('===== run One-mode projection =====')
    
    query_end = end_time.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
    start_time = end_time - datetime.timedelta(hours = 1)
    query_start = start_time.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")

    print('end time: ' + query_end)

    run_main = main.Main()
    run_main.run(query_start, query_end)


def run_filter(nexttime):
    print('===== run pcap to csv =====')
    print(datetime.datetime.now())
    
    run_main = main.Main()
    run_main.runPcapToCsc(nexttime)


def timerFun(sched_timer):

    next_time = '2020-05-13T00:00:00.000000+08:00'
    nexttime = datetime.datetime.strptime(next_time, '%Y-%m-%dT%H:%M:%S.%f+08:00')
    
    while True:
        nowtime = datetime.datetime.now()
        #nowtime = datetime.datetime.strptime("2020-05-07T17:00:00.000000+08:00", '%Y-%m-%dT%H:%M:%S.%f+08:00')
        if nexttime > nowtime:
            sleeptime = (nexttime - nowtime).seconds
            time.sleep(sleeptime)
        
        run_filter(nexttime)
        
        if nexttime.strftime("%M") == '00':
            if nexttime >= sched_timer:
                run_task(nexttime)
        
        nexttime = nexttime + datetime.timedelta(minutes = 15)
        
        
if __name__ == '__main__':
    
    # print(datetime.datetime.now())
        
    # print(os.getcwd())
    path = os.getcwd() + '/data/'
    # print(path)
    print(os.listdir(path))
    
    start = "2020-05-07T22:00:00.000000+08:00"
    sched_timer = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%f+08:00')
    # sched_timer = datetime.datetime.now() + datetime.timedelta(minutes = 15)

    print('run the timer task at: ' + str(sched_timer))
    timerFun(sched_timer)
    
