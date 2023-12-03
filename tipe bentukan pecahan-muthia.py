#Nama: Muthia Zhafira Sahnah 
#NIM: 24060122130071
#Tugas praktikum tipe bentukan pecahan


class MakeP:
    def __init__(self,pembilang,penyebut):
        self.x = pembilang
        self.y = penyebut

def pembilang(P):
    return P.x

def penyebut(P):
    return P.y

def IsEqP(P1,P2):
    return pembilang(P1)==pembilang(P2) and penyebut(P1)==penyebut(P2)

def IsLtP(P1,P2):
     return (pembilang(P1)*penyebut(P2))<(penyebut(P1)*pembilang(P2))

def IsGtP(P1,P2):
    return(pembilang(P1)*penyebut(P2))>(penyebut(P1)*pembilang(P2))

def AddP(P1,P2):
    return((penyebut(P2)*pembilang(P1))+(penyebut(P1)*pembilang(P2)))/(penyebut(P1)*penyebut(P2))

def Sub(P1,P2):
    return((penyebut(P2)*pembilang(P1))-(penyebut(P1)*pembilang(P2)))/(penyebut(P1)*penyebut(P2))

def Mul(P1,P2):
    return((pembilang(P1)*pembilang(P2)))/((penyebut(P1)*penyebut(P2)))

def Div(P1,P2):
    return(((pembilang(P1)*penyebut(P2)))/(penyebut(P1)*pembilang(P2)))

def Real(P):
    return(pembilang(P)/penyebut(P))

P1 = MakeP(2,4)
P2 = MakeP(2,6)
print(IsEqP(P1, P2))
print(IsGtP(P1, P2))
print(IsLtP(P1,P2))
print(AddP(P1, P2))
print(Sub(P1, P2))
print(Mul(P1, P2))
print(Div(P1, P2))
print(Real(P1))