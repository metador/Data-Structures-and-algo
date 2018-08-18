import sys

class MarbleBoard:
    marbles_list=[]
    def __init__(self,argv):
        self.marbles_list =argv
        #print argv;

    def switch(self):
        a=self.marbles_list[0]
        self.marbles_list[0]=self.marbles_list[1]
        self.marbles_list[1]=a

    def rotate(self):
        temp = self.marbles_list[0]
        self.marbles_list.append(temp)
        self.marbles_list.pop(0)

    def is_solved(self):
        for i in range(0,len(self.marbles_list)-1):
            if self.marbles_list[i]<self.marbles_list[i+1]:
                continue
            else:
                return False
        return True

    def __str__(self):
        return " ".join(map(lambda x:str(x),self.marbles_list))

class Solver:
    board =[]
    def __init__(self,board):
     self.solve(board)

    def solve(self,board):
        counter=0
        while not board.is_solved():
            print board
            for i in range(0,len(board.marbles_list)-1):
                if board.marbles_list[0] < board.marbles_list[1]:
                    if not board.is_solved():
                        board.rotate()
                        counter+=1
                        print board
                else:
                    if board.marbles_list[1] == 0:
                        board.rotate()
                        counter +=1
                        print board
                    else:
                        board.switch()
                        counter +=1
                        print board
        print "total steps: "+str(counter)

#print MarbleBoard(sys.argv).is_solved()



marbles_list=[]
try:
    if len(sys.argv[1:])==1:
        print "there"
        marbles_list = map(lambda x: int(x), sys.argv[1:][0].split(","))
    else:
        marbles_list = map(lambda x: int(x), sys.argv[1:])
    #print map(lambda x: int(x), sys.argv[1:][0].split(","))
except:

    print "input not int"

s = Solver(MarbleBoard(marbles_list))
#validation(sys.argv)



#if __name__== "__main__":
#   MarbleBoard(sys.argv[1:])
