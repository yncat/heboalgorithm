# https://atcoder.jp/contests/abc085/tasks/abc085_c

import sys


def parseCMDLine():
    papers = int(sys.argv[1])
    amount = int(sys.argv[2])
    return papers, amount


def isPossible(papers, amount):
    if amount < papers*1000:
        return False
    if amount > papers*10000:
        return False
    return True


def printImpossible():
    print("そんなのは嘘です。あり得ません")


def search(papers, amount):
    for i in range(papers+1):
        for j in range(papers+1):
            if i+j > papers:
                break
            p1000 = i
            p5000 = j
            p10000 = papers-i-j
            if (p1000*1000) + (p5000*5000) + (p10000)*10000 == amount:
                return (p1000, p5000, p10000)


def printResult(ret):
    print("、".join(["%sが%d枚" % (i, j) for i, j in zip(
        ["1000円札", "5000円札", "10000円札"], ret) if j > 0]) + "あったんですね!")


papers, amount = parseCMDLine()
if not isPossible(papers, amount):
    printImpossible()
    sys.exit(0)
# end impossible

ret = search(papers, amount)
if not ret:
    printImpossible()
    sys.exit()
# end impossible
printResult(ret)
