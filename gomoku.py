import numpy as np
import sys

class Gomoku():
    def __init__(self):
        self.BoardSize_y = 9
        self.BoardSize_x = 9
        self.Blank = 0
        self.Black = 1
        self.White = 2
        self.reset()
    
    def reset(self):
        self.cells = np.zeros([self.BoardSize_y,self.BoardSize_x])

    def get_cell(self,action):
        y = action[0]
        x = action[1]
        return self.cells[y][x]

    def set_cell(self,action,color):
        y = int(action[0])
        x = int(action[1])
        try:
            self.cells[y][x] = int(color)
            return True
        except:
            return False

    def PrintBoard(self):
        s = " "
        for i in range(0,self.BoardSize_x):
            s = s + " " + str(i)
        print(s)
        for i in range(0,self.BoardSize_y):
            cy = str(i)
            for j in range(0,self.BoardSize_x):
                cx = ""
                if self.cells[i][j] == self.Black:
                    cx = "○"
                elif self.cells[i][j] == self.White:
                    cx = "●"
                else:
                    cx = "*"
                cy = cy + " " + cx
            print(cy)
    
    # 置ける場所リスト
    def EnableList(self):
        l = []
        for i in range(0,self.BoardSize_y):
            for j in range(0,self.BoardSize_x):
                if self.cells[i][j] == self.Blank:
                    l.insert(0,str(i) + str(j))
        return l

    def WinCheck(self,action,color):
        y = int(action[0])
        x = int(action[1])
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                cy = i
                cx = j
                cnt = 1
                if i == 0 and j == 0:
                    continue
                while True:
                    if self.cells[y + cy][x + cx] == color:
                        cnt = cnt + 1
                    else:
                        break
                    print(cnt)
                    if cnt >= 5:
                        return True
                    cy = cy + i
                    cx = cx + j
        return False


# テスト用ゲーム処理
if __name__ == "__main__":
    env = Gomoku()
    print("---GAME START---")
    EndFlag = False
    player = 0
    while EndFlag == False:
        for i in (1,2):
            player = i
            flg = False
            inp = ""
            while flg == False:
                if env.Black == i:
                    print("先行のターン○")
                elif env.White == i:
                    print("後攻のターン●")
                env.PrintBoard()
                print("石をおく場所を入力して下さい。exitでゲーム終了")
                inp = input(">>>")
                if str(inp) == "exit":
                    sys.exit()
                for e in env.EnableList():
                    if e == inp:
                        flg = env.set_cell(inp,i)
                if flg == False:
                    print("正しい値を入力して下さい")
            EndFlag = env.WinCheck(inp,i)
            if EndFlag == True:
                break
    print("---GAME OVER---")
    env.PrintBoard()
    if player == env.Black:
        print("先行プレイヤーの勝ちです◯")
    else:
        print("後攻プレイヤーの勝ちです●")


