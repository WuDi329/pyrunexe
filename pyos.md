## menu structure & output
test1 => os.popen  ==> ['helloworld\n']
test2 => commands.getstatusoutput  ==>  rc = 0, out = helloworld
test3 => os.system ==>  
helloworld
0


## os system
- system函数可以将字符串转化成命令在服务器上运行；其原理是每一条system函数执行时，其会创建一个子进程在系统上执行命令行，子进程的执行结果无法影响主进程
- 上述原理会导致当需要执行多条命令行的时候可能得不到预期的结果；
- 为了保证system执行多条命令可以成功，多条命令需要在同一个子进程中运行；

##  os popen
- os.popen() 功能强于os.system()
- 通过 os.popen() 返回的是 file read 的对象，对其进行读取 read() 的操作可以看到执行的输出。

## commands getstatusoutput
- 通过 commands.getstatusoutput() 一个方法就可以获得到返回值和输出


 https://cloud.tencent.com/developer/article/1486996
