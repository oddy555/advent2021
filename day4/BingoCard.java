package day4;

public class BingoCard {

    private BingoPos bingoCard[][] = new BingoPos[5][5];
    public boolean isWinner;

    public BingoCard(BingoPos[][] b) {
        bingoCard = b;
        isWinner = false;
    }

    public boolean toDuttCheck(int val) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (bingoCard[i][j].val == val) {
                    bingoCard[i][j].dutted = true;
                    return true;
                }
            }
        }
        return false;
    }

    private boolean checkRow(int row) {
        int duttCount = 0;
        for (int i=0; i < 5; i++) {
            if (bingoCard[row][i].dutted == true) {
                duttCount++;
            }
        }
        if (duttCount == 5) {
            return true;
        } else {
            return false;
        }
    }

    private boolean checkCol(int col) {
        int duttCount = 0;
        for (int i=0; i < 5; i++) {
            if (bingoCard[i][col].dutted == true) {
                duttCount++;
            }
        }
        if (duttCount == 5) {
            return true;
        } else {
            return false;
        }
    }

    public boolean checkBingo() {
        for (int i = 0; i < 5; i++) {
            if (checkRow(i)) {
                isWinner = true;
                return true;
            } else if (checkCol(i)) {
                isWinner = true;
                return true;   
            }
        }
        return false;
    }

    public int getUnduttedSum() {
        int sum = 0;
        for (int i = 0; i < 5; i++){
            for (int j = 0; j < 5; j++) {
                if (bingoCard[i][j].dutted == false) {
                    sum += bingoCard[i][j].val;
                }    
            }    
        }
        return sum;
    }
}
