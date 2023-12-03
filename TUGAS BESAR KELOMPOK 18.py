# KELOMPOK 18
# ANGGOTA KELOMPOK:
# 1. Mohamad Faisal Rizki 24060122130068 (KELAS A)
# 2. Ahmad Fahrezi 24060122140146 (Kelas C)
# 3. Muthia Zhafira Sahnah 24060122130071 (Kelas D)
# 4. Muhammad Anshar Al Faruq 24060122140148 (Kelas A)



# ===========================================================
# ========================FUNGSI=============================
class PohonBiner:
    def __init__(self,A, L=None, R=None):
        self.A= A
        self.L = L
        self.R = R
    def __repr__(self):
        return "(%s, (%s, %s)" % (repr(self.A), repr(self.L), repr(self.R))
    
def Akar(P):
    return P.A
def Left(P):
    return P.L
def Right(P):
    return P.R

def MakePB(A, L=None, R=None):
    return PohonBiner(A, L, R)

def IsEmpty(P):
    if P == None:
        return True
    else:
        return False

def IsOneElement(P):
    if IsEmpty(P):
        return False
    elif IsEmpty(Left(P)) and IsEmpty(Right(P)):
        return True
    else:
        return False

def ReRefix(P):
    if IsEmpty(P):
        return []
    elif IsOneElement(P):
        return [Akar(P)]
    else:
        return ReRefix(Left(P)) + [Akar(P)] + ReRefix(Right(P))

def NBElmt(P):
    if IsEmpty(P):
        return 0
    elif IsOneElement(P):
        return 1
    else:
        return NBElmt(Left(P)) + NBElmt(Right(P)) + 1

def makeprefix(X):
    if IsEmpty(X):
        return []
    elif IsOneElement(X):
        return [Akar(X)]
    else:
        return [Akar(X)] + [makeprefix(Left(X))] + [makeprefix((Right(X)))]

def isEmptyLOL(S):
    return S == []

def nbElmtList(S):
    if isinstance(S, list):
        if isEmptyLOL(S):
            return 0
        else:
            return 1 + nbElmtList(tailList(S))
    else:
        return 1

def isOneElmt(S):
    return nbElmtList(S) == 1

def firstList(S):
    if isinstance(S, list):
        return S[0]
    else:
        return S

def tailList(S):
    return S[1:]
    
# ======================================================================

PB = MakePB(20,MakePB(11,MakePB(3,MakePB(1,None,None),MakePB(7,None,None)),MakePB(13,MakePB(12,None,None),MakePB(17,None,None))),MakePB(30,MakePB(26,MakePB(24,None,None),MakePB(29,None,None)),MakePB(35,MakePB(34,None,None),MakePB(38,None,None))))
#print(makeprefix(PB))
print(ReRefix(PB))

print("Total pembelian tiket KAI bulan Desember: ", NBElmt(PB))

# =======================================================================
def pembagianbawah(L):
    if isEmptyLOL(L):
        return 0 
    else:
        if firstList(L) <=1 :
            return 1 + pembagianbawah(tailList(L))
        else:
            return pembagianbawah(tailList(L))
            

print("Dibawah umur: ", pembagianbawah(ReRefix(PB)))
# =======================================================================

def pembagianbalita(L):
    if isEmptyLOL(L):
        return 0 
    else:
        if firstList(L) >1 and firstList(L) <=5 :
            return 1 + pembagianbawah(tailList(L))
        else:
            return pembagianbawah(tailList(L))
            

print("Balita: ", pembagianbalita(ReRefix(PB)))
# =======================================================================

def pembagiananak(L):
    if isEmptyLOL(L):
        return 0 
    else:
        if firstList(L) > 5 and firstList(L) <= 12:
            return 1 + pembagiananak(tailList(L))
        else:
            return pembagiananak(tailList(L))
            

print("Anak-anak: ", pembagiananak(ReRefix(PB)))
# =======================================================================
def pembagiandewasa(L):
    if isEmptyLOL(L):
        return 0 
    else:
        if firstList(L) > 12:
            return 1 + pembagiandewasa(tailList(L))
        else:
            return pembagiandewasa(tailList(L))
            

print("Anak-anak: ", pembagiandewasa(ReRefix(PB)))
# =======================================================================

def hargatiket(L):
    if isEmptyLOL(L):
        return 0
    else:
        if firstList(L) <= 1 :
            return (0 + hargatiket(tailList(L)))
        elif firstList(L) > 1 and firstList(L) <= 5:
            return (50000 + hargatiket(tailList(L)))
        elif firstList(L) > 5 and firstList(L) <= 12:
            return (75000 + hargatiket(tailList(L)))
        else:
            return (100000 + hargatiket(tailList(L)))

print ("Jumlah penjualan tiket KAI pada bulan Desember: ",(hargatiket(ReRefix(PB))))

