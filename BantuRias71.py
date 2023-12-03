#Muthia Zhafira Sahnah
#24060122130071

berapaTestcase = input()
TestCase1 = [int(x) for x in input().split()]
TestCase2 = [int(x) for x in input().split()]
TestCase3 = [int(x) for x in input().split()]

def BantuRias(TestCase1,TestCase2,TestCase3):
    return ((TestCase1[1]-TestCase1[0])*100) + ((TestCase2[1]-TestCase2[0])*100) + ((TestCase3[1]-TestCase3[0])*100)

print(BantuRias(TestCase1, TestCase2, TestCase3))


