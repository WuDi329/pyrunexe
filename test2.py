import commands
import os

def cc():
    main="./hello"
    if os.path.exists(main):
        rc, out = commands.getstatusoutput(main)
        print 'rc = %d, \nout = %s' % (rc, out)


if __name__ == '__main__':
    cc()

