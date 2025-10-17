import numpy as np

class HField():
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
            

    def reset(self, seed=None, options=None):

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
