import os

def cc():
    main="./hello"
    if os.path.exists(main):
        r_v = os.system(main)
        print r_v


if __name__ == '__main__':
    cc()


