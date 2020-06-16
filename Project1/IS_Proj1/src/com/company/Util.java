package com.company;

public class Util {
    public static int[][] convertStringTo2DArray(String inputString) throws Exception{
        int[][] arr = new int[3][3];
        inputString=inputString.replace("{","");
        inputString=inputString.substring(0,inputString.length()-2);
        //System.out.println(inputString);

        String rows[] = inputString.split("},");
        for(int i=0;i<rows.length;i++) {
            //System.out.println(rows[i]);
            String cols[] = rows[i].trim().split(",");
            for(int j=0;j<cols.length;j++) {
                arr[i][j] = Integer.parseInt(cols[j].trim());
            }
        }
        return arr;
    }

    public static boolean isMatched(int[][] state, int[][] goal_state) {
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(state[i][j]!=goal_state[i][j])
                    return false;
            }
        }
        return true;
    }

    public static int[][] copyMat(int[][] input_state) {
        int[][] nextstate = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                nextstate[i][j] = input_state[i][j];
            }
        }
        return nextstate;
    }

    public static void printMat(int[][] nextstate) {

        for (int i = 0; i < 3; i++) {
            System.out.print("\t");
            for (int j = 0; j < 3; j++) {
                System.out.print(nextstate[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static String matToString(int[][] nextstate) {
        StringBuilder sb=new StringBuilder();
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                sb.append(nextstate[i][j]);
            }
        }
        return sb.toString();
    }
    public static int[][] stringToMatrix(String s){
        int[][] mat = new int[3][3];
        int index =0;
        int i=0;
        while(index<s.length()){

            for(int j=0;j<3;j++){
                mat[i][j]=Integer.parseInt(s.charAt(index)+"");
                index++;
            }
            i++;
            /*mat[0][0]=Integer.parseInt(s.charAt(index++)+"");
            mat[0][1]=Integer.parseInt(s.charAt(index++)+"");
            mat[0][2]=Integer.parseInt(s.charAt(index++)+"");
            mat[1][0]=Integer.parseInt(s.charAt(index++)+"");
            mat[1][1]=Integer.parseInt(s.charAt(index++)+"");
            mat[1][2]=Integer.parseInt(s.charAt(index++)+"");
            mat[2][0]=Integer.parseInt(s.charAt(index++)+"");
            mat[2][1]=Integer.parseInt(s.charAt(index++)+"");
            mat[2][2]=Integer.parseInt(s.charAt(index++)+"");*/
        }
        for(char c: s.toCharArray()){

        }

        return mat;
    }

}
