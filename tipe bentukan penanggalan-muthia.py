#Nama: Muthia Zhafira Sahnah 
#NIM: 24060122130071
#Tugas praktikum tipe bentukan penanggalan

class Hr:
    def __init__(self,hari):
        self.hari = hari

class Bln:
    def __init__(self,bulan):
        self.bulan = bulan

class Thn:
    def __init__(self,tahun):
        self.tahun = tahun

class date(Hr,Bln,Thn):
    def __init__(self,hari,bulan,tahun):
        Hr.__init__(self,hari)
        Bln.__init__(self,bulan)
        Thn.__init__(self, tahun)

def Day(D):
    return D.hari

def Month(D):
    return D.bulan

def Year(D):
    return D.tahun


def Nextday(D):
    if Month(D) == 1 or Month(D) ==3 or Month(D) == 5 or Month(D)==7 or Month(D) == 8 or Month(D) == 10:
        if Day(D)<31:
            return date(Day(D)+1,Month(D),Year(D))
        elif Day(D)==31:
            return date(1,Month(D)+1,Year(D))
    elif Month(D)==2:
        if IsKabisat(D) == True:
            if Day(D)<29:
                return date(Day(D)+1, Month(D), Year(D))
            elif Day(D)==29:
                return date(1,Month(D)+1,Year(D))
        else:
            if Day(D)<28:
                return date(Day(D)+1, Month(D), Year(D))
            elif Day(D)==28:
                return date(1,Month(D)+1, Year(D))
    elif Month(D)==4 or Month(D)==6 or Month(D)==9 or Month(D)==11:
        if Day(D)<30:
            return date(Day(D)+1, Month(D),Year(D))
        elif Day(D)==30:
            return date(1,Month(D)+1,Year(D))
    elif Month(D)==12:
        if Day(D)<31:
            return date(Day(D)+1, Month(D),Year(D))
        elif Day(D)==31:
            return date(1,1,Year(D)+1)
    else:
        return False


def Yesterday(D):
    if Day(D) == 1:
        if Month(D) == 12 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10:
            return date(30, Month(D) - 1, Year(D))
        elif Month(D) == 2:
            return date(31, Month(D) -1, Year (D))
        elif Month(D) == 3:
            if (Year(D) % 4 == 0 and Year(D)%100 !=0) or Year(D)%400 == 0:
                return date(29, 2, Year(D))
            else:
                return date(28, 2, Year(D))
        elif Month(D) == 4 or Month(D) == 6 or Month(D) == 9 or Month(D) == 11:
            return date(31, Month(D), Year(D))
        elif Month(D) == 1:
            return date(31, 12, Year(D) - 1)
    else:
        return date(Day(D) - 1, Month(D), Year(D))


def NextNday(D,N):
    if N ==1:
        return Nextday(D)
    else:
        return NextNday(Nextday(D),N-1)

def dpm(b):
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 60
    elif b == 4:
        return 91
    elif b == 5:
        return 121
    elif b == 6:
        return 152
    elif b == 7:
        return 182
    elif b == 8:
        return 213
    elif b == 9:
        return 244
    elif b == 10:
        return 274
    elif b == 11:
        return 305
    elif b == 12:
        return 335
    else:
        return "Tidak Valid"

def HariKe1900(D):
    return Day(D) + dpm(Month(D)) if Month(D) > 2 and IsKabisat(D) == True  else Day(D) - 1 + dpm(Month(D))

def IsEqD(D1,D2):
    return Day(D1)==Day(D2) and Month(D1)==Month(D2) and Year(D1)==Year(D2)

def IsBefore(D1,D2):
    if Year(D1)<Year(D2):
       return True
    if Year(D1)==Year(D2):
       return True if HariKe1900(D1)<HariKe1900(D2) else False
    else:
        return False

def IsAfter(D1,D2):
    if Year(D1)>Year(D2):
        return True
    if Year(D1)==Year(D2):
        return True if HariKe1900(D1)>HariKe1900(D2) else False
    else:
        False

def IsKabisat(D):
    return Year(D)%4==0 and Year(D)%4!=0 or Year(D)%400==0

D1 = date(26,11,2003)
D2 = date(16,7,2004)
print(IsEqD(D1, D2))
print(IsBefore(D1, D2))
print(IsAfter(D1, D2))
print(IsKabisat(D1))
print("{},{},{}".format(Day(Nextday(D1)),Month(Nextday(D1)),Year(Nextday(D1))))
print("{},{},{}".format(Day(Yesterday(D2)),Month(Yesterday(D2)),Year(Yesterday(D2))))
print("{},{},{}".format(Day(NextNday(D1,3)),Month(NextNday(D1,3)),Year(NextNday(D1,3))))



