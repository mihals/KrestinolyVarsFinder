import numpy as np

class NField():
    def __init__(self):
        # набор карт в колоде
        self.cardSet = []
        # for i in range(4):
        #     self.cardSet.append(i*2+1)
        #     self.cardSet.append(i*2+2)
        #     self.cardSet.append(i*2+1+9)
        #     self.cardSet.append(i*2+2+9)
        #     self.cardSet.append(i*2+1+18)
        #     self.cardSet.append(i*2+2+18)
        #     self.cardSet.append(i*2+1+27)
        #     self.cardSet.append(i*2+2+27)

        # self.cardSet.append(9)
        # self.cardSet.append(18)
        # self.cardSet.append(27)
        # self.cardSet.append(36)

        for i in range(1,10):
            self.cardSet.append(i)
            self.cardSet.append(i+9)
            self.cardSet.append(i+18)
            self.cardSet.append(i+27)
            

    def reset(self, restore = False):

        if restore:
            self.observation_space = np.array([26, 27, 35,  7, 36,  8,  9,  0, 34, 25, 36])
            self.actions = [0, np.int64(1), np.int64(2), np.int64(4), np.int64(6), np.int64(8), np.int64(5), np.int64(7), np.int64(3), np.int64(3), np.int64(0), np.int64(9), np.int64(5), np.int64(6), np.int64(9), np.int64(4), np.int64(2), np.int64(0), np.int64(3), np.int64(7), np.int64(0), np.int64(2), np.int64(6), np.int64(9), np.int64(3), np.int64(5), np.int64(9), np.int64(8), np.int64(5), np.int64(4), np.int64(0), np.int64(2), np.int64(6), np.int64(7), np.int64(1), np.int64(4)]
            self.states = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 2], [1, 10, 19, 0, 0, 0, 0, 0, 0, 0, 3], [1, 10, 19, 0, 28, 0, 0, 0, 0, 0, 4], [1, 10, 19, 0, 28, 0, 2, 0, 0, 0, 5], [1, 10, 19, 0, 28, 0, 2, 0, 11, 0, 6], [1, 10, 19, 0, 28, 20, 2, 0, 11, 0, 7], [1, 10, 19, 0, 28, 20, 2, 29, 11, 0, 8], [1, 10, 19, 3, 28, 20, 2, 29, 11, 0, 9], [0, 10, 19, 12, 28, 20, 0, 29, 11, 0, 10], [21, 10, 19, 12, 28, 20, 0, 29, 11, 0, 11], [0, 10, 0, 12, 28, 0, 0, 29, 11, 30, 12], [0, 10, 0, 12, 0, 4, 0, 0, 11, 0, 13], ([ 0, 10,  0, 12,  0,  4, 13,  0, 11,  0, 14]), ([ 0, 10,  0, 12,  0,  4, 13,  0, 11, 22, 15]), ([ 0, 10,  0, 12, 31,  4, 13,  0, 11, 22, 16]), ([ 0, 10,  5, 12, 31,  4, 13,  0, 11, 22, 17]), ([14, 10,  5, 12, 31,  4, 13,  0, 11, 22, 18]), ([ 0, 10,  5, 23, 31,  4,  0,  0, 11, 22, 19]), ([ 0, 10,  5, 23, 31,  4,  0, 32, 11, 22, 20]), ([ 6, 10,  5, 23, 31,  4,  0, 32, 11, 22, 21]), ([ 0, 10, 15, 23, 31,  0,  0, 32, 11, 22, 22]), ([ 0, 10, 15, 23, 31,  0, 24, 32, 11, 22, 23]), ([ 0, 10, 15,  0, 31,  0,  0, 32, 11, 33, 24]), ([ 0, 10, 15,  7,  0,  0,  0,  0, 11,  0, 25]), ([ 0, 10, 15,  7,  0, 16,  0,  0, 11,  0, 26]), ([ 0, 10,  0,  7,  0,  0,  0,  0,  0, 25, 27]), ([ 0, 10,  0,  7,  0,  0,  0,  0, 34, 25, 28]), ([ 0, 10,  0,  7,  0,  8,  0,  0, 34, 25, 29]), ([ 0, 10,  0,  7, 17,  8,  0,  0, 34, 25, 30]), ([26, 10,  0,  7, 17,  8,  0,  0, 34, 25, 31]), ([26, 10, 35,  7, 17,  8,  0,  0, 34, 25, 32]), ([26, 10, 35,  7, 17,  8,  9,  0, 34, 25, 33]), ([26, 10, 35,  7, 17,  8,  9, 18, 34, 25, 34]), ([26, 27, 35,  7,  0,  8,  9,  0, 34, 25, 35]), ([26, 27, 35,  7, 36,  8,  9,  0, 34, 25, 36])]
            self.maxStep = 0
            self.minCard = 7
            return
            
             #[0, np.int64(1), np.int64(2), np.int64(4), np.int64(6), np.int64(8), np.int64(5), np.int64(7), np.int64(3), np.int64(3), np.int64(0), np.int64(9), np.int64(5), np.int64(4), np.int64(9), np.int64(6), np.int64(0), np.int64(7), np.int64(4), np.int64(1), np.int64(2), np.int64(2), np.int64(7), np.int64(4), np.int64(9), np.int64(5), np.int64(8), np.int64(7), np.int64(7), np.int64(0), np.int64(2), np.int64(1), np.int64(4), np.int64(4), np.int64(5), np.int64(2)]
            #array([17, 35, 36, 12, 18,  0, 31,  0,  0,  0, 36])
            #[array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), array([ 1, 10,  0,  0,  0,  0,  0,  0,  0,  0,  2]), array([ 1, 10, 19,  0,  0,  0,  0,  0,  0,  0,  3]), array([ 1, 10, 19,  0, 28,  0,  0,  0,  0,  0,  4]), array([ 1, 10, 19,  0, 28,  0,  2,  0,  0,  0,  5]), array([ 1, 10, 19,  0, 28,  0,  2,  0, 11,  0,  6]), array([ 1, 10, 19,  0, 28, 20,  2,  0, 11,  0,  7]), array([ 1, 10, 19,  0, 28, 20,  2, 29, 11,  0,  8]), array([ 1, 10, 19,  3, 28, 20,  2, 29, 11,  0,  9]), array([ 0, 10, 19, 12, 28, 20,  0, 29, 11,  0, 10]), array([21, 10, 19, 12, 28, 20,  0, 29, 11,  0, 11]), array([ 0, 10,  0, 12, 28,  0,  0, 29, 11, 30, 12]), array([ 0, 10,  0, 12,  0,  4,  0,  0, 11,  0, 13]), array([ 0, 10,  0, 12, 13,  4,  0,  0, 11,  0, 14]), array([ 0, 10,  0, 12, 13,  4,  0,  0, 11, 22, 15]), array([ 0, 10,  0, 12, 13,  4, 31,  0, 11, 22, 16]), array([ 5, 10,  0, 12, 13,  4, 31,  0, 11, 22, 17]), array([ 5, 10,  0, 12, 13,  4, 31, 14, 11, 22, 18]), array([ 5,  0,  0, 12, 23,  4, 31,  0, 11, 22, 19]), array([ 5, 32,  0, 12, 23,  4, 31,  0, 11, 22, 20]), array([ 5, 32,  6, 12, 23,  4, 31,  0, 11, 22, 21]), array([ 0, 32, 15, 12, 23,  0, 31,  0, 11, 22, 22]), array([ 0, 32, 15, 12, 23,  0, 31, 24, 11, 22, 23]), array([ 0, 32, 15, 12, 33,  0, 31,  0, 11,  0, 24]), array([ 0, 32, 15, 12, 33,  0, 31,  0, 11,  7, 25]), array([ 0, 32, 15, 12, 33, 16, 31,  0, 11,  7, 26]), array([ 0, 32,  0, 12, 33,  0, 31,  0, 25,  7, 27]), array([ 0, 32,  0, 12, 33,  0, 31, 34, 25,  7, 28]), array([ 0,  0,  0, 12,  0,  0, 31,  8, 25,  7, 29]), array([17,  0,  0, 12,  0,  0, 31,  8, 25,  7, 30]), array([17,  0, 26, 12,  0,  0, 31,  8, 25,  7, 31]), array([17, 35, 26, 12,  0,  0, 31,  8, 25,  7, 32]), array([17, 35, 26, 12,  9,  0, 31,  8, 25,  7, 33]), array([17, 35, 26, 12, 18,  0, 31,  0, 25,  0, 34]), array([17, 35, 26, 12, 18, 27, 31,  0, 25,  0, 35]), array([17, 35, 36, 12, 18,  0, 31,  0,  0,  0, 36])]


        self.observation_space = np.array([0,0,0,0,0,0,0,0,0,0,0], dtype=int)
        self.maxStep = 0
        self.minCard = 0
        # номер ячейки, в которую надо добавить следующую карту
        self.action_space = 0

        self.states, self.actions, self.rewards = [], [], []
        self.states.append(np.copy(self.observation_space))
        self.actions.append(0)
        
        return self.observation_space 
    
    def setNextCard(self) -> bool:
        if(self.observation_space[-1] == 0):
             self.observation_space[0] = 1
             self.observation_space[-1] =1
             return True
        
        self.addCard()

        if self.observation_space[10] == 36:
            zeroIndArr = np.where(self.observation_space == 0)[0]
            if zeroIndArr.size > self.minCard:
                 self.minCard = zeroIndArr.size
            if zeroIndArr.size == 10: 
                return False
            
            return False
        
        zeroIndArr = np.where(self.observation_space == 0)[0]
        
        if zeroIndArr.size == 0: return False
        if self.observation_space[10] == 36: return False
        card = self.cardSet[self.observation_space[10]]
        
        zeroInd = zeroIndArr[0]
        # следующая карта в колоде
        self.observation_space[zeroInd] = card
        self.actions.append(zeroInd)
        self.observation_space[10]+=1
        self.states.append(np.copy(self.observation_space))
        if(self.observation_space[-1] > self.maxStep):
             self.maxStep = self.observation_space[-1]
        return True
    
    """ откатываемся к предыдущим состояниям, если зашли в тупик"""
    def rollback(self) -> bool:
        if len(self.actions) == 0:
            return False
        else: 
            self.states.pop()
            self.actions.pop()
            self.observation_space = np.copy(self.states[-1])
            return True
        
    """ переставляем предыдущую карту на новое место"""
    def replace(self):
        self.observation_space = np.copy(self.states[-1])
        # удаляем ряды, если они есть
        #self.addCard()
        
        # находим индексы свободных (нулевых) полей
        indOfZero = np.where(self.observation_space == 0)[0]

        # если свободных полей нет - тупик, выходим
        if indOfZero.size == 0: return False

        # последняя добавленная карта, находим её индекс
        card = self.observation_space[self.actions[-1]]
        indOfCard = np.where(self.observation_space == card)[0]
        if indOfCard.size == 0 : return False

        # проверяем есть ли свободные поля правее последней карты
        nextZeroInd = np.where(indOfZero > indOfCard[0])[0]
        if nextZeroInd.size == 0: return False

        # если свободное поле найдено, переставляем карту
        newPlace = indOfZero[nextZeroInd[0]]
        self.observation_space[newPlace] = card
        self.observation_space[indOfCard[0]] = 0
        self.states[-1] = np.copy(self.observation_space)
        self.actions[-1] = newPlace
        return True
    
    # возвращает масть по номеру карты в колоде, номера начинаются с 1 
    def getSuitByNum(self, numOfCard:int) -> int:
        if (numOfCard - 1)//9 == 0:
            return 0
        elif (numOfCard - 1)//9 == 1:
            return 1
        elif (numOfCard - 1)//9 == 2:
            return 2
        return 3
    
    #TODO добавить проверку по диагонали
    # нумерация полей слева направо, сверху вниз
    def addCard(self):
        # if self.observation_space[10] == 0:
        #     self.observation_space[0] = self.cardSet[0]
        #     self.observation_space[-1] = 1
        #     return True  
        # узнаём по номеру в колоде карту
        card = np.int64(self.cardSet[self.observation_space[-1] - 1])

        # ищем позицию этой карты в состоянии, исключаем последнее
        # значение, чтобы случайно не совпало значение
        posArr = np.where(self.observation_space == card)[0]
        if posArr.size != 0 and posArr[0] != len(self.observation_space) - 1:
            pos = posArr[0]
        else:
            return False
        
        isLine = False
        # верхняя точка на левой ножке
        if(pos == 0):
            posSuit = self.getSuitByNum(self.observation_space[0])
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            if (self.observation_space[2] != 0 and
                self.observation_space[5] != 0 and
                self.getSuitByNum(self.observation_space[2]) == posSuit
                and
                self.getSuitByNum(self.observation_space[5]) == posSuit):
                self.observation_space[2] = 0
                self.observation_space[5] = 0
                isLine = True
                # если есть ряд из трёх карт, проверяем нет
                # ли четырёх
                if(self.getSuitByNum(self.observation_space[8]) == posSuit):
                    self.observation_space[8] = 0
            

            # проверяем диагональ
            if (self.observation_space[3] != 0 and
                self.observation_space[6] != 0 and
                self.getSuitByNum(self.observation_space[3]) == posSuit
                and
                self.getSuitByNum(self.observation_space[6]) == posSuit):
                    self.observation_space[3] = 0
                    self.observation_space[6] = 0
                    isLine = True
                    # проверяем на ряд из четырёх по диагонали
                    if(self.getSuitByNum(self.observation_space[9]) == posSuit):
                        self.observation_space[9] = 0
            if isLine: self.observation_space[0] = 0
        
        # вторая сверху точка на левой ножке
        if(pos == 2):
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт, ячейка может быть как крайней в ряду, так и
            # в середине ряда
            posSuit = self.getSuitByNum(self.observation_space[2])
            if ((self.observation_space[0] != 0 and
                self.observation_space[5] != 0 and
                self.getSuitByNum(self.observation_space[0]) == posSuit
                and
                self.getSuitByNum(self.observation_space[5]) == posSuit)
                or
                (self.observation_space[5] != 0 and
                self.observation_space[8] != 0 and
                self.getSuitByNum(self.observation_space[5]) == posSuit
                and
                self.getSuitByNum(self.observation_space[8]) == posSuit)):
                    isLine = True
                    if(self.getSuitByNum(self.observation_space[0]) == posSuit):
                         self.observation_space[0] = 0
                    if(self.getSuitByNum(self.observation_space[5]) == posSuit):
                         self.observation_space[5] = 0
                    if(self.getSuitByNum(self.observation_space[8]) == posSuit):
                         self.observation_space[8] = 0
            if isLine: self.observation_space[2] = 0

        # третья сверху точка на левой ножке
        if(pos == 5):
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            posSuit = self.getSuitByNum(self.observation_space[5]) 
            if ((self.observation_space[2] != 0 and
                self.observation_space[8] != 0 and
                self.getSuitByNum(self.observation_space[2]) == posSuit
                and
                self.getSuitByNum(self.observation_space[8]) == posSuit)
                or
                (self.observation_space[2] != 0 and
                self.observation_space[0] != 0 and
                self.getSuitByNum(self.observation_space[2]) == posSuit
                and
                self.getSuitByNum(self.observation_space[0]) == posSuit)):
                    isLine = True
                    if(self.getSuitByNum(self.observation_space[0]) == posSuit):
                         self.observation_space[0] = 0
                    if(self.getSuitByNum(self.observation_space[2]) == posSuit):
                         self.observation_space[2] = 0
                    if(self.getSuitByNum(self.observation_space[8]) == posSuit):
                         self.observation_space[8] = 0
            if isLine: self.observation_space[5] = 0
                    

        # четвёртая сверху точка на левой ножке
        if(pos == 8):
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            if (self.observation_space[2] != 0 and
                self.observation_space[5] != 0 and
                self.getSuitByNum(self.observation_space[5]) == \
                self.getSuitByNum(self.observation_space[8]) and
                self.getSuitByNum(self.observation_space[2]) == \
                self.getSuitByNum(self.observation_space[8])):
                    self.observation_space[2] = 0
                    self.observation_space[5] = 0
                    isLine = True
                    # если есть ряд из трёх карт, проверяем нет
                    # ли четырёх
                    if(self.getSuitByNum(self.observation_space[0]) == \
                       self.getSuitByNum(self.observation_space[8])):
                        self.observation_space[0] = 0
                    self.observation_space[8] = 0

        # верхняя точка на правой ножке
        if(pos == 1):
            posSuit = self.getSuitByNum(self.observation_space[1]) 
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            if (self.observation_space[4] != 0 and
                self.observation_space[7] != 0 and
                self.getSuitByNum(self.observation_space[4]) == posSuit
                and
                self.getSuitByNum(self.observation_space[7]) == posSuit):
                    self.observation_space[4] = 0
                    self.observation_space[7] = 0
                    isLine = True
                    # если есть ряд из трёх карт, проверяем нет
                    # ли четырёх
                    if self.getSuitByNum(self.observation_space[9]) == posSuit:
                        self.observation_space[9] = 0
            if isLine:
                 self.observation_space[1] = 0
                 
        # вторая сверху точка на правой ножке
        if(pos == 4):
            posSuit = self.getSuitByNum(self.observation_space[4])
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            if ((self.observation_space[1] != 0 and
                self.observation_space[7] != 0 and
                self.getSuitByNum(self.observation_space[1]) == posSuit
                and
                self.getSuitByNum(self.observation_space[7]) == posSuit)
                or
                (self.observation_space[7] != 0 and
                self.observation_space[9] != 0 and
                self.getSuitByNum(self.observation_space[7]) == posSuit
                and
                self.getSuitByNum(self.observation_space[9]) == posSuit)):
                    isLine = True
                    if self.getSuitByNum(self.observation_space[1]) == posSuit:
                         self.observation_space[1] = 0
                    if self.getSuitByNum(self.observation_space[7]) == posSuit:
                         self.observation_space[7] = 0
                    if self.getSuitByNum(self.observation_space[9]) == posSuit:
                         self.observation_space[9] = 0

            if isLine:
                 self.observation_space[4] = 0
        
        # третья сверху точка на правой ножке
        if(pos == 7):
            posSuit = self.getSuitByNum(self.observation_space[7]) 
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            if ((self.observation_space[4] != 0 and
                self.observation_space[1] != 0 and
                self.getSuitByNum(self.observation_space[4]) == posSuit
                and
                self.getSuitByNum(self.observation_space[1]) == posSuit)
                or
                (self.observation_space[4] != 0 and
                self.observation_space[9] != 0 and
                self.getSuitByNum(self.observation_space[4]) == posSuit
                and
                self.getSuitByNum(self.observation_space[9]) == posSuit)):
                    isLine = True
                    if self.getSuitByNum(self.observation_space[1]) == posSuit:
                         self.observation_space[1] = 0
                    if self.getSuitByNum(self.observation_space[4]) == posSuit:
                         self.observation_space[4] = 0
                    if self.getSuitByNum(self.observation_space[9]) == posSuit:
                         self.observation_space[9] = 0
                    self.observation_space[7] = 0

        # нижняя точка на правой ножке
        if (pos == 9):
            posSuit = self.getSuitByNum(self.observation_space[9])
            # проверяем есть ли вертикальный ряд хотя бы из
            # трёх карт
            if (self.observation_space[7] != 0 and
                self.observation_space[4] != 0 and
                self.getSuitByNum(self.observation_space[4]) == posSuit
                and
                self.getSuitByNum(self.observation_space[7]) == posSuit):
                isLine = True
                self.observation_space[4] = 0
                self.observation_space[7] = 0
                # проверяем ряд на четвёртую карту
                if(self.observation_space[1] != 0 and
                    self.getSuitByNum(self.observation_space[1]) == posSuit):
                    self.observation_space[1] = 0
                
            
            # проверяем диагональ
            if (self.observation_space[6] != 0 and
                self.observation_space[3] != 0 and
                self.getSuitByNum(self.observation_space[6]) == posSuit
                and
                self.getSuitByNum(self.observation_space[3]) == posSuit):
                isLine = True
                self.observation_space[6] = 0
                self.observation_space[3] = 0
                # проверяем ряд на четверной ряд
                if(self.observation_space[0] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == posSuit):
                    self.observation_space[0] = 0
            if isLine:
                 self.observation_space[9] = 0
        
        # верхняя левая точка на перекладине
        if (pos == 3):
            posSuit = self.getSuitByNum(self.observation_space[3])
            # проверяем на диагональ
            if (self.observation_space[0] != 0 and
                self.observation_space[6] != 0 and
                self.getSuitByNum(self.observation_space[0]) == posSuit
                and
                self.getSuitByNum(self.observation_space[6]) == posSuit):
                isLine = True
                self.observation_space[0] = 0
                self.observation_space[6] = 0
                # проверяем ряд на четверной ряд
                if(self.observation_space[9] != 0 and
                    self.getSuitByNum(self.observation_space[9]) == posSuit):
                    self.observation_space[9] = 0

            if isLine:
                self.observation_space[3] = 0

        # нижняя правая точка на перекладине
        if (pos == 6):
            posSuit = self.getSuitByNum(self.observation_space[6])
            # проверяем на диагональ
            if (self.observation_space[9] != 0 and
                self.observation_space[3] != 0 and
                self.getSuitByNum(self.observation_space[9]) == posSuit
                and
                self.getSuitByNum(self.observation_space[3]) == posSuit):
                isLine = True
                self.observation_space[9] = 0
                self.observation_space[3] = 0
                # проверяем ряд на четверной ряд
                if(self.observation_space[0] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == posSuit):
                    self.observation_space[0] = 0

            if isLine:
                self.observation_space[6] = 0

        if isLine:
             return


