#-*-coding:utf-8-*-
import time
for i in range(0,1000):
    with open("ceshi.txt","a",encoding='utf-8') as f:
        f.write(str(i)+"\n")
        print(i)
        time.sleep(1)