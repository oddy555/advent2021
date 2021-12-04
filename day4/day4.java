package day4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class Day4 {
    public static void main(String[] args) {
        ArrayList<BingoCard> bingoCards = new ArrayList<BingoCard>();
        String tombola = "";
        try {
            File f = new File("E:/programmering/advent2021/day4/input.txt");
            Scanner s = new Scanner(f);
            s.useDelimiter("\n");
            tombola = s.next();
            
            
            while (s.hasNext())  {
                s.next();
                BingoPos bingoCard[][] = new BingoPos[5][5];
                for (int i = 0; i < 5; i++) {

                    String tmp = s.next();
                    Scanner tmpS = new Scanner(tmp);
                    for (int j = 0; j < 5; j++) {
                        bingoCard[i][j] = new BingoPos(tmpS.nextInt());      
                    }
                    tmpS.close();
                }
                bingoCards.add(new BingoCard(bingoCard));
                
            }
            s.close();


        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        }

        Scanner s = new Scanner(tombola);
        s.useDelimiter(",");
        int lastProd = 0;
        int lastNum = 0;
        
        while (s.hasNext()) {
            int num = s.nextInt();
            for (int i = 0; i < bingoCards.size(); i++) {
                BingoCard bc = bingoCards.get(i);
                if (bc.isWinner == true) {
                    continue;
                }
                bc.toDuttCheck(num);
                if (bc.checkBingo()) {
                    lastNum = num;
                    lastProd = num * bc.getUnduttedSum();
                    String output = "BINGO!!!; Current number: " + Integer.toString(lastNum) + " prod: " + Integer.toString(lastProd);
                    System.out.println(output);
                }
            }
            if (!s.hasNextInt()) {
                String output = "LAST BINGO is!!!; Current number: " + Integer.toString(lastNum) + " prod: " + Integer.toString(lastProd);
                System.out.println(output);
                s.close();
                return;
            }
        }

        s.close();
    }
}