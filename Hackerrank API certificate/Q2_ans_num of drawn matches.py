
import requests
import time
from multiprocessing import Process, Value, Lock


class Counter(object):
    def __init__(self, initval=0):
        self.val = Value('i', initval)
        self.lock = Lock()

    def increment(self,v):
        with self.lock:
            self.val.value += v

    def value(self):
        with self.lock:
            return self.val.value

def hello_there(num__):
        
        total=0
        num_=num__[1]
        year=num__[2]
        url="https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&page="
        for ctr in range(num_,num_+5):
            response = requests.get(url+str(ctr))
            response.raise_for_status()
            jsonResponse = response.json()
            for key, value in jsonResponse.items():
                if(key=='data'):
                    for v in value:
                        if(v['team1goals']==v['team2goals']):
                            total=total+1
        num__[0].increment(total)

def main(year):
        counter = Counter(0)
        url="https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&page="
        response = requests.get(url+str('1'))
        response.raise_for_status()
        jsonResponse = response.json()
        num_=0
        for key, value in jsonResponse.items():
            if(key=='total_pages'):
                num_=value
                break
        n=1

        jobs = []
        ret_value=None
        while(n<num_+5):
            process = Process(target=hello_there,args=([counter,n,year],))
            jobs.append(process) 
            n=n+5

        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
        print(counter.value())

if __name__ == '__main__':
    main('2011')