import numpy as np

class LCS:
    # Constructor
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.__table = np.full((len(s1)+1, len(s2)+1),-1)

        # berisi u, l(left), dan d(diagonal)
        self.__tableCursor = np.full((len(s1)+1, len(s2)+1),'n')


    # Melakukan penelusuran dan mengembalikan panjang dari lcs
    def lcsLong(self):
        a = len(self.s1)
        b = len(self.s2)
        for i in range(a+1):
            for j in range(b+1):
                if(i==0 or j==0):
                    self.__table[i][j] = 0
                elif(self.s1[i-1]==self.s2[j-1]):
                    self.__table[i][j] = 1 + self.__table[i-1][j-1]
                    self.__tableCursor[i][j] = 'd'
                elif self.__table[i-1][j]>=self.__table[i][j-1]:
                    self.__table[i][j] = self.__table[i-1][j]
                    self.__tableCursor[i][j] = 'u'
                else:
                    self.__table[i][j] = self.__table[i][j-1]
                    self.__tableCursor[i][j] = 'l'
        return self.__table[a][b]


    # Print tabel yang terbentuk dari penelusuran lcs
    def printTable(self):
        if self.isEmptyTable():
            self.lcs()

        print('    ', end='')
        for i in self.s2:
            print('', i, end=' ')
        print()

        for i in range(len(self.__table)):
            if i != 0: print(self.s1[i-1], end=' ')
            else: print(' ', end=' ')

            for j in range(len(self.__table[i])):
                print(self.__table[i][j], end='')
                if(j!=0 and i!=0): print(self.__tableCursor[i][j], end=' ')
                else: print(' ', end=' ')

            print()
        print('\nu:up   d:diagonal   l:left\n')

    def printTableCursor(self):
        for i in range(len(self.__tableCursor)):
            print(self.__tableCursor[i])



    # Print subsquence hasil dari penelusuran lcs
    def lcs(self):
        self.__lcs(len(self.s1),len(self.s2))
        print()

    def __lcs(self,i,j):
          if self.isEmptyTable():
              self.lcs()

          if i==0 or j==0: return

          if self.__tableCursor[i][j]=='d':
              self.__lcs(i-1,j-1)
              print(self.s1[i-1],end='')
          elif self.__tableCursor[i][j]=='u':
              self.__lcs(i-1,j)
          else: self.__lcs(i,j-1)



    # Cek jika tabel masih kosong atau masih belum dilakukan penelusuran
    def isEmptyTable(self):
        return self.__table[0][0] == -1



    # Print kedua squence, panjang lcs, subsquence, dan tabel hasi penelusuran
    def detail(self):
        print('Squence:')
        print(self.s1)
        print(self.s2)
        print('---------------------------------------------------------------')
        print('Long   :',self.lcsLong())
        print('LCS    :',end=' ')
        self.lcs()
        print('Table  :')
        self.printTable()


test = LCS('qwerfaw','dsfgihqwe')
test.detail()

test2 = LCS('ASD','DSAD')
test2.detail()

test3 = LCS('aspdofndvib','asdfghjkl')
test3.detail()

test4 = LCS('bacf','abcef')
test4.detail()

test5 = LCS('ABCBDAB','BDCABA')
test5.detail()

test6 = LCS('qwertiopasnj210567tyu567kjljkl9', 'givvafbkonbjhbnmzwercfvtgbyhnjmk0987')
test6.detail()