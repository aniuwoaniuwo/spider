from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        #ip池程序启动入口
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
