import os

def cc():
    main="./hello"
    f = os.popen(main)
    data = f.readlines()
    f.close()
    return data


if __name__ == '__main__':
    print(cc())
