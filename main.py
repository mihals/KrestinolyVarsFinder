from enum import Enum
import gymnasium as gym
import numpy as np
from nField import NField

nf = NField()
nf.reset(True)
done = True
counter = 0
nextCall = "set"
#array([26, 10, 17, 25, 18, 34, 35, 27, 36,  0, 36])
#[0, np.int64(1), np.int64(2), np.int64(4), np.int64(6), np.int64(8), np.int64(5), np.int64(7), np.int64(3), np.int64(3), np.int64(0), np.int64(9), np.int64(5), np.int64(6), np.int64(9), np.int64(7), np.int64(2), np.int64(0), np.int64(3), np.int64(4), np.int64(0), np.int64(2), np.int64(6), np.int64(9), np.int64(7), np.int64(5), np.int64(3), np.int64(5), np.int64(4), np.int64(2), np.int64(0), np.int64(6), np.int64(9), np.int64(4), np.int64(7), np.int64(8)]
#[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 2], [1, 10, 19, 0, 0, 0, 0, 0, 0, 0, 3], [1, 10, 19, 0, 28, 0, 0, 0, 0, 0, 4], [1, 10, 19, 0, 28, 0, 2, 0, 0, 0, 5], [1, 10, 19, 0, 28, 0, 2, 0, 11, 0, 6], [1, 10, 19, 0, 28, 20, 2, 0, 11, 0, 7], [1, 10, 19, 0, 28, 20, 2, 29, 11, 0, 8], [1, 10, 19, 3, 28, 20, 2, 29, 11, 0, 9], [0, 10, 19, 12, 28, 20, 0, 29, 11, 0, 10], [21, 10, 19, 12, 28, 20, 0, 29, 11, 0, 11], [0, 10, 0, 12, 28, 0, 0, 29, 11, 30, 12], [0, 10, 0, 12, 0, 4, 0, 0, 11, 0, 13], [0, 10, 0, 12, 0, 4, 13, 0, 11, 0, 14], [0, 10, 0, 12, 0, 4, 13, 0, 11, 22, 15], array([ 0, 10,  0, 12,  0,  4, 13, 31, 11, 22, 16]), array([ 0, 10,  5, 12,  0,  4, 13, 31, 11, 22, 17]), array([14, 10,  5, 12,  0,  4, 13, 31, 11, 22, 18]), array([ 0, 10,  5, 23,  0,  4,  0, 31, 11, 22, 19]), array([ 0, 10,  5, 23, 32,  4,  0, 31, 11, 22, 20]), array([ 6, 10,  5, 23, 32,  4,  0, 31, 11, 22, 21]), array([ 0, 10, 15, 23, 32,  0,  0, 31, 11, 22, 22]), array([ 0, 10, 15, 23, 32,  0, 24, 31, 11, 22, 23]), array([ 0, 10, 15,  0, 32,  0,  0, 31, 11, 33, 24]), array([ 0, 10, 15,  0,  0,  0,  0,  7, 11,  0, 25]), array([ 0, 10, 15,  0,  0, 16,  0,  7, 11,  0, 26]), array([ 0, 10,  0, 25,  0,  0,  0,  7,  0,  0, 27]), array([ 0, 10,  0, 25,  0, 34,  0,  7,  0,  0, 28]), array([ 0, 10,  0, 25,  8, 34,  0,  7,  0,  0, 29]), array([ 0, 10, 17, 25,  8, 34,  0,  7,  0,  0, 30]), array([26, 10, 17, 25,  8, 34,  0,  7,  0,  0, 31]), array([26, 10, 17, 25,  8, 34, 35,  7,  0,  0, 32]), array([26, 10, 17, 25,  8, 34, 35,  7,  0,  9, 33]), array([26, 10, 17, 25, 18, 34, 35,  0,  0,  0, 34]), array([26, 10, 17, 25, 18, 34, 35, 27,  0,  0, 35]), array([26, 10, 17, 25, 18, 34, 35, 27, 36,  0, 36])]


# лучший результат - осталось 3 карты
[0, np.int64(1), np.int64(2), np.int64(4), np.int64(6), np.int64(8), np.int64(5), np.int64(7), np.int64(3), np.int64(3), np.int64(0), np.int64(9), np.int64(2), np.int64(6), np.int64(9), np.int64(4), np.int64(5), np.int64(0), np.int64(3), np.int64(7), np.int64(0), np.int64(2), np.int64(6), np.int64(3), np.int64(0), np.int64(5), np.int64(8), np.int64(9), np.int64(2), np.int64(4), np.int64(9), np.int64(6), np.int64(5), np.int64(7), np.int64(1), np.int64(0)]
while done:
        counter += 1

        if counter == 990:
            done = True
        if(nf.observation_space[0] == 0):
            done = True
        if(len(nf.states) == 10):
            done = True
        if(np.where(nf.observation_space == 2)[0].size == 2):
            done = True
        if(nf.maxStep == 36):
            done = True
        if np.array_equal([0, np.int64(1), np.int64(2), np.int64(4), np.int64(6), np.int64(8), np.int64(5), np.int64(9), np.int64(3), np.int64(3), np.int64(0), np.int64(7), np.int64(2), np.int64(6), np.int64(9), np.int64(4), np.int64(5), np.int64(0), np.int64(3), np.int64(7), np.int64(0), np.int64(5), np.int64(6), np.int64(3), np.int64(0), np.int64(2), np.int64(2), np.int64(9), np.int64(4), np.int64(5), np.int64(7)],#, np.int64(7), np.int64(0), np.int64(2), np.int64(3), np.int64(9)],
                          nf.actions):
            done = True


        if nextCall == "set":
            if nf.setNextCard():
                nextCall = "set"
            else : 
                nextCall = "rollback"
        elif nextCall == "rollback":
            if nf.rollback():
                nextCall = "replace"
            else: done = True
        elif nextCall == "replace":
            if nf.replace():
                nextCall = "set" 
            else : nextCall = "rollback"

class GridWorldEnv(gym.Env):

    def __init__(self):

        self.states, self.actions, self.rewards = [], [], []
        self.numEqArr = 0
        self.directTray = False
        self.backTrace = False
        # поле 3x3 в виде одномерного массива, последний элемент равен
        # числу выставленных карт, начинаем с выставленного в ячейку 0
        # первой карты
        #self.observation_space = spaces.Box(0,9, dtype= int)

        # номер поля для добавления карты
        #self.action_space = spaces.Discrete(9)

        # набор карт в колоде
        self.cardSet = []

        for i in range(4):
            self.cardSet.append(i*2+1)
            self.cardSet.append(i*2+2)
            self.cardSet.append(i*2+1+9)
            self.cardSet.append(i*2+2+9)
            self.cardSet.append(i*2+1+18)
            self.cardSet.append(i*2+2+18)
            self.cardSet.append(i*2+1+27)
            self.cardSet.append(i*2+2+27)

        self.cardSet.append(9)
        self.cardSet.append(18)
        self.cardSet.append(27)
        self.cardSet.append(36)
        
        return
        for i in range(0,36):
            if i%4 == 0:
                cardSuit = 0
            elif i%4 == 1:
                cardSuit = 1
            elif i%4 == 2:
                cardSuit = 2
            else: cardSuit = 3
            cardVal = i//4 +1
            self.cardSet.append(cardSuit*9 + cardVal)

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        # первую карту выкладываем в ячейку 0
        self.observation_space = np.array([1,0,0,0,0,0,0,0,0,1], dtype=int)
        # номер ячейки, в которую надо добавить следующую карту
        self.action_space = 0

        self.states, self.actions, self.rewards = [], [], []
        self.states.append(np.copy(self.observation_space))
        self.actions.append(0)
        self.rewards.append(0)
        

        # observation = self._get_obs()
        # info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        #self.startEpisode()

        return self.observation_space 
    
    def startEpisode(self):
        state = self.getAction()
        self.states.append(state)

    # выбирает место, куда положить карту, начиная с поля 1 (поле
    # 0 занято с самого начала) и до поля 8
    def getAction(self):
        if(self.action_space == 8):
            if(self.observation_space[9] == 18):
                return self.observation_space, self.action_space
            else:
                freeCells = np.where(self.observation_space != 0)
                
            
        if(self.observation_space[9] == 1):
            arr = np.where(self.observation_space != 0)
            return


    def step(self, action):
        self.addCard()
        
        # если action == 0, ищем новое место для текущей карты
        if(action == 0):
            # количество использованных карт 
            cardVal = self.observation_space[9]
            # ищем свободные поля
            indOfZero = np.where(self.observation_space == 0)[0]
            # если есть свободные поля, ищем те, индекс которых больше
            # индекса поля, которое занимает карта
            if(indOfZero.size != 0):
                # индекс карты
                indOfCard = np.where(self.observation_space == cardVal)[0][0]
                # свободное поле с индексом больше, чем индекс карты
                nextZeroInd = np.where(indOfZero > indOfCard)[0]
                # если подходящих полей нет, возвращаемся к предыдущей карте
                if nextZeroInd.size == 0:
                    while self.states[-1][9] == cardVal:
                        del self.states[-1]
                        del self.actions[-1]
                        del self.rewards[-1]
                    # возвращаемся назад и ищем другое место для
                    # предыдущей карты
                    self.observation_space = np.copy(self.states[-1])
                    self.action_space = 0
                    return self.observation_space, 0, False, False, {}
                else:
                    self.observation_space[indOfCard] = 0
                    self.observation_space[indOfZero[nextZeroInd[0]]] = cardVal
                    self.action_space = 1
                    self.states.append(np.copy(self.observation_space))
                    self.actions.append(self.action_space)
                    self.rewards.append(0)
                    return self.observation_space, 0, False, False, {}
            # если свободных мест нет
            else:
                while self.states[-1][9] == cardVal:
                    del self.states[-1]
                    del self.actions[-1]
                    del self.rewards[-1]
                # возвращаемся назад и ищем другое место для
                # предыдущей карты
                self.observation_space = np.copy(self.states[-1])
                self.action_space = 0
                return self.observation_space, 0, False, False, {}    
        # ищем место для следующей карты
        else:
            cardVal = self.cardSet[self.observation_space[9]]
            indOfZero = np.where(self.observation_space == 0)[0]
            if(indOfZero.size == 0):
                while self.states[-1][9] == cardVal:
                    del self.states[-1]
                    del self.actions[-1]
                    del self.rewards[-1]

                self.action_space = 0
                self.observation_space = np.copy(self.states[-1])
                return self.observation_space, 0, False, False, {}
            else:
                self.observation_space[indOfZero[0]] = self.cardSet[self.observation_space[9]]
                self.observation_space[9] = self.observation_space[9]+1
                self.action_space = 1
                self.states.append(np.copy(self.observation_space))
                self.actions.append(self.action_space)
                self.rewards.append(0)
                return self.observation_space, 0, False, False, {}

    

    ''' в списке  self.observations хранятся несокращенные состояния,
     образовавшиеся ряды, если они есть, ещё не удалены, ряды удаляются
     лишь в self.observation_space в этом методе'''
    def addCard(self):
        usedCards = self.observation_space[9]
        
        # узнаём по номеру в колоде карту
        card = np.int64(self.cardSet[self.observation_space[9] - 1])

        # ищем позицию этой карты в состоянии, исключаем последнее
        # значение, чтобы случайно не совпало значение
        pos = np.where(self.observation_space == card)[0]
        if pos.size != 0 and pos[0] != 9:
            card = pos[0]
        else:
            return False
        
        nRow:int = pos[0]//3
        nCol:int = pos[0]%3
        
        if nRow == 0:
            isLine = False
            
            if nCol == 0:
                # проверяем по вертикали
                if (self.observation_space[3] != 0 and
                    self.observation_space[6] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[3]) and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[6])):
                    self.observation_space[3] = 0
                    self.observation_space[6] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[1] != 0 and
                    self.observation_space[2] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[1]) and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[2])):
                    self.observation_space[1] = 0
                    self.observation_space[2] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                # проверяем по диагонали
                if (self.observation_space[4] != 0 and
                    self.observation_space[8] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[8])):
                    self.observation_space[4] = 0
                    self.observation_space[8] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                if isLine: self.observation_space[0] = 0

            if nCol == 1:
                # проверяем по вертикали
                if (self.observation_space[4] != 0 and
                    self.observation_space[7] != 0 and
                    self.getSuitByNum(self.observation_space[1]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[1]) == \
                        self.getSuitByNum(self.observation_space[7])):
                    self.observation_space[4] = 0
                    self.observation_space[7] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[0] != 0 and
                    self.observation_space[2] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[1]) and
                    self.getSuitByNum(self.observation_space[1]) == \
                        self.getSuitByNum(self.observation_space[2])):
                    self.observation_space[0] = 0
                    self.observation_space[2] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                if isLine: self.observation_space[1] = 0

            if nCol == 2:
                # проверяем по вертикали
                if (self.observation_space[5] != 0 and
                    self.observation_space[8] != 0 and
                    self.getSuitByNum(self.observation_space[2]) == \
                        self.getSuitByNum(self.observation_space[5]) and
                    self.getSuitByNum(self.observation_space[2]) == \
                        self.getSuitByNum(self.observation_space[8])):
                    self.observation_space[5] = 0
                    self.observation_space[8] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[0] != 0 and
                    self.observation_space[1] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[2]) and
                    self.getSuitByNum(self.observation_space[1]) == \
                        self.getSuitByNum(self.observation_space[2])):
                    self.observation_space[0] = 0
                    self.observation_space[1] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                # проверяем по диагонали
                if (self.observation_space[4] != 0 and
                    self.observation_space[6] != 0 and
                    self.getSuitByNum(self.observation_space[4]) == \
                        self.getSuitByNum(self.observation_space[2]) and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[2])):
                    self.observation_space[4] = 0
                    self.observation_space[6] = 0
                    #self.observation_space[2] = 0
                    isLine = True

                if isLine: self.observation_space[2] = 0
            
        if nRow == 1:
            isLine = False
            
            if nCol == 0:
                # проверяем по вертикали
                if (self.observation_space[0] != 0 and
                    self.observation_space[6] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[3]) and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[3])):
                    self.observation_space[0] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[6] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[4] != 0 and
                    self.observation_space[5] != 0 and
                    self.getSuitByNum(self.observation_space[4]) == \
                        self.getSuitByNum(self.observation_space[3]) and
                    self.getSuitByNum(self.observation_space[5]) == \
                        self.getSuitByNum(self.observation_space[3])):
                    self.observation_space[4] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[5] = 0
                    isLine = True

                if isLine: self.observation_space[3] = 0

            if nCol == 1:
                # проверяем по вертикали
                if (self.observation_space[1] != 0 and
                    self.observation_space[7] != 0 and
                    self.getSuitByNum(self.observation_space[1]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[7]) == \
                        self.getSuitByNum(self.observation_space[4])):
                    self.observation_space[1] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[7] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[3] != 0 and
                    self.observation_space[5] != 0 and
                    self.getSuitByNum(self.observation_space[3]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[5]) == \
                        self.getSuitByNum(self.observation_space[4])):
                    self.observation_space[3] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[5] = 0
                    isLine = True

                # проверяем по диагоналям
                if (self.observation_space[0] != 0 and
                    self.observation_space[8] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[8]) == \
                        self.getSuitByNum(self.observation_space[4])):
                    self.observation_space[0] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[8] = 0
                    isLine = True

                if (self.observation_space[2] != 0 and
                    self.observation_space[6] != 0 and
                    self.getSuitByNum(self.observation_space[2]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[4])):
                    self.observation_space[2] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[6] = 0
                    isLine = True

                if isLine: 
                    self.observation_space[4] = 0
            
            if nCol == 2:
                # проверяем по вертикали
                if (self.observation_space[2] != 0 and
                    self.observation_space[8] != 0 and
                    self.getSuitByNum(self.observation_space[2]) == \
                        self.getSuitByNum(self.observation_space[5]) and
                    self.getSuitByNum(self.observation_space[8]) == \
                        self.getSuitByNum(self.observation_space[5])):
                    self.observation_space[2] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[8] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[3] != 0 and
                    self.observation_space[4] != 0 and
                    self.getSuitByNum(self.observation_space[3]) == \
                        self.getSuitByNum(self.observation_space[5]) and
                    self.getSuitByNum(self.observation_space[5]) == \
                        self.getSuitByNum(self.observation_space[4])):
                    self.observation_space[3] = 0
                    #self.observation_space[3] = 0
                    self.observation_space[4] = 0
                    isLine = True

                if isLine: self.observation_space[5] = 0
            
        if nRow == 2:
            isLine = False
            
            if nCol == 0:
                # проверяем по вертикали
                if (self.observation_space[0] != 0 and
                    self.observation_space[3] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[6]) and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[3])):
                    self.observation_space[0] = 0
                    self.observation_space[3] = 0
                    #self.observation_space[6] = 0
                    isLine = True

                # проверяем по горизонтали
                if (self.observation_space[7] != 0 and
                    self.observation_space[8] != 0 and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[7]) and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[8])):
                    self.observation_space[7] = 0
                    self.observation_space[8] = 0
                    #self.observation_space[6] = 0
                    isLine = True

                # проверяем по диагонали
                if (self.observation_space[4] != 0 and
                    self.observation_space[2] != 0 and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[4]) and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[2])):
                    self.observation_space[4] = 0
                    self.observation_space[2] = 0
                    #self.observation_space[6] = 0
                    isLine = True

                if isLine: self.observation_space[6] = 0

            if nCol == 1:
                # проверяем по вертикали   
                if (self.observation_space[1] != 0 and
                    self.observation_space[4] != 0 and
                    self.getSuitByNum(self.observation_space[1]) == \
                        self.getSuitByNum(self.observation_space[7]) and
                    self.getSuitByNum(self.observation_space[7]) == \
                        self.getSuitByNum(self.observation_space[4])):
                        self.observation_space[1] = 0
                        self.observation_space[4] = 0
                        #self.observation_space[7] = 0
                        isLine = True

                # проверяем по горизонтали   
                if (self.observation_space[6] != 0 and
                    self.observation_space[8] != 0 and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[7]) and
                    self.getSuitByNum(self.observation_space[7]) == \
                        self.getSuitByNum(self.observation_space[8])):
                        self.observation_space[6] = 0
                        self.observation_space[8] = 0
                        #self.observation_space[7] = 0

                if isLine: self.observation_space[7] = 0
                
            if nCol == 2:
                # проверяем по вертикали  
                if (self.observation_space[2] != 0 and
                    self.observation_space[5] != 0 and
                    self.getSuitByNum(self.observation_space[2]) == \
                        self.getSuitByNum(self.observation_space[8]) and
                    self.getSuitByNum(self.observation_space[8]) == \
                        self.getSuitByNum(self.observation_space[5])):
                    self.observation_space[2] = 0
                    self.observation_space[5] = 0
                    #self.observation_space[8] = 0
                    isLine = True

                # проверяем по горизонтали  
                if (self.observation_space[6] != 0 and
                    self.observation_space[7] != 0 and
                    self.getSuitByNum(self.observation_space[6]) == \
                        self.getSuitByNum(self.observation_space[8]) and
                    self.getSuitByNum(self.observation_space[8]) == \
                        self.getSuitByNum(self.observation_space[7])):
                    self.observation_space[6] = 0
                    self.observation_space[7] = 0
                    #self.observation_space[8] = 0
                    isLine = True

                # проверяем по диагонали  
                if (self.observation_space[0] != 0 and
                    self.observation_space[4] != 0 and
                    self.getSuitByNum(self.observation_space[0]) == \
                        self.getSuitByNum(self.observation_space[8]) and
                    self.getSuitByNum(self.observation_space[8]) == \
                        self.getSuitByNum(self.observation_space[4])):
                    self.observation_space[0] = 0
                    self.observation_space[4] = 0
                    #self.observation_space[8] = 0
                    isLine = True

                if isLine: self.observation_space[8] = 0

            if isLine:
                #self.observation_space[9] += 1
                self.action_space = 1

    def setNextCard(self) -> bool:
        self.addCard()

        if self.observation_space[9] == 36:
            zeroIndArr = np.where(self.observation_space == 0)[0]
            if zeroIndArr.size == 9: 
                return False
            
            return False
            self.directTray = False
            indOfZero = np.where(self.observation_space == 0)
            if indOfZero[0].size == 9:
                return False
        #self.observation_space = np.array([ 0, 22, 15,  8, 26,  0,  7, 14,  0, 24])
        # ищем свободное место                                                                                                                                                                                                                                                                                                                                                                                                                                              
        zeroIndArr = np.where(self.observation_space == 0)[0]
        if zeroIndArr.size >= 6: 
                self.directTray = True
        
        if zeroIndArr.size == 0: return False
        if self.observation_space[9] == 36: return False
        card = self.cardSet[self.observation_space[9]]
        
        zeroInd = zeroIndArr[0]
        # следующая карта в колоде
        self.observation_space[zeroInd] = card
        self.actions.append(zeroInd)
        self.observation_space[9]+=1
        self.states.append(np.copy(self.observation_space))
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
        
    def _rollback(self) -> bool:
        if self.states[-1][9] == 1:
            return False
        else: 
            self.states.pop()
            self.actions.pop()
            #self.states[-1][9] -= 1
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
        self.observation_space[indOfCard] = 0
        self.states[-1] = np.copy(self.observation_space)
        self.actions[-1] = newPlace
        return True
    
    def _replace(self):
        self.observation_space = np.copy(self.states[-1])
        self.addCard()
        indOfZero = np.where(self.observation_space == 0)[0]
        if indOfZero.size == 0: return False
        card = self.cardSet[self.observation_space[-1]-1]
        
        #TODO предусмотреть случай, когда количество использованных
        # карт совпадает с номером карты, т.е. 
        # self.observation_space[9] == card
        indOfCard = np.where(self.observation_space == card)[0]
        if indOfCard.size == 0 : return False
        nextZeroInd = np.where(indOfZero > indOfCard[0])[0]
        
        if nextZeroInd.size == 0: return False
        newPlace = indOfZero[nextZeroInd[0]]
        self.observation_space[newPlace] = card
        self.observation_space[indOfCard] = 0
        self.observation_space[9] += 1
        self.states.append(np.copy(self.observation_space))
        self.actions[-1] = newPlace
        return True


    # возвращает карту по её номеру(начиная с 1) в колоде
    def getCardByNum(self, numOfCard:int):
        cardVal = (numOfCard -1)%9 +1
        cardSuit = (numOfCard-1)//9
        return (cardSuit*9 + cardVal)
    
    # возвращает масть по номеру карты в колоде, номера начинаются с 1 
    def getSuitByNum(self, numOfCard:int) -> int:
        if (numOfCard - 1)//9 == 0:
            return 0
        elif (numOfCard - 1)//9 == 1:
            return 1
        elif (numOfCard - 1)//9 == 2:
            return 2
        return 3
    
    def checkActionsSample(self, actions):
        
        #if len(actionsSample) != 0:
            # for i in range(len(actionsSample)):
            #     if np.array_equal(actions, actionsSample[i]):
            #         self.numEqArr += 1
            #         actionsSample.append(np.copy(actions))
            #     else:
            #         continue
            actionsSample.append(np.copy(actions)[17:-1])

episodes = 10
myGWE = GridWorldEnv()
numEqArr = 0

for episode in range(1, episodes+1):
    state = myGWE.reset()
    
    done = False
    nextCall = "set" 
    actionsSample = []
    counter = 0
    myGWE.directTray = True
    minRBack = 27
    
    while myGWE.directTray:
        action = myGWE.action_space
        counter += 1
        # if myGWE.observation_space[9] == 27:
        #     indOfZero = np.where(myGWE.observation_space == 0)
        #     if indOfZero[0].size == 9:
        #         done = True
        #     else: nextCall = "rollback"

        # if (len(myGWE.actions) >= 17 and
        #     myGWE.actions[15] == myGWE.actions[16] == 2):
        #     done = False

        # if np.array_equal([12, 22,  0, 21, 24,  7, 16, 14, 15, 17],
        #                   myGWE.observation_space):
        #     done = False

        #array([ 0, 22, 15,  8, 26,  0,  7, 14,  0, 24])
        #array([ 0, 22, 15, 18, 26,  0,  0, 14,  0, 26])
        #array([ 0, 22, 15,  8, 26,  0,  7, 14,  0, 24])
        
        # if myGWE.observation_space[5] == 18:
        #     print("18")
        # фото для акшн = 20
        # после коунтер 97
        if counter == 17:
                    minRBack = len(myGWE.actions)

        zeroIndArr = np.where(myGWE.observation_space == 0)[0]
        if zeroIndArr.size >= 9: 
            minRBack = len(myGWE.actions)

        if nextCall == "set":
            if myGWE.setNextCard():
                nextCall = "set"
            else : 
                nextCall = "rollback"
                # if myGWE.observation_space[9] == 27:
                #     #myGWE.checkActionsSample(myGWE.actions)
                #     indOfZero = np.where(myGWE.observation_space == 0)
                #     nextCall = "rollback"
                #     if indOfZero[0].size >= 5:
                #         done = True
                # else: nextCall = "rollback"
        elif nextCall == "rollback":
            if myGWE.rollback():
                if len(myGWE.actions) < minRBack:
                    minRBack = len(myGWE.actions)

                nextCall = "replace"
            else: done = True
        elif nextCall == "replace":
            if myGWE.replace():
                nextCall = "set" 
            else : nextCall = "rollback"

        # if len(myGWE.actions) > 18:
        #     myGWE.checkActionsSample(myGWE.actions)

    #myGWE.backTrace = True
    backAnchor = 26
    nextCall = "rollback"
    while myGWE.backTrace:
        if nextCall == "rollback":
            if myGWE.rollback():
                nextCall = "replace"
        elif nextCall == "replace":
            if(myGWE.replace()):
                nextCall = "replace"
            else:
                nextCall = "rollback"

        #n_state, reward, done, val, info = myGWE.step(action)



