package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    static ArrayList<String> visited = new ArrayList<>();
    static PriorityQueue<State> statesToBeExpanded = new PriorityQueue<>();
    static boolean debug = false;
    static int nodeGenerated = 0;

    public static void main(String[] args) throws IOException {
        //int[][] input_state = {{1, 2, 3}, {4, 8, 0}, {7, 6, 5}};
        //int[][] goal_state = {{1, 2, 3}, {4, 5,6}, {7, 8, 0}};
        //int[][] input_state = {{1, 2, 3}, {7, 4,5}, {6,8, 0}};
        //int[][] goal_state={{1,2,3},{8,6,4},{7,5,0}};
        //int[][] input_state = {{2, 8, 1}, {3, 4,6}, {7,5,0}};
        //int[][] goal_state={{3,2,1},{8,0,4},{7,5,6}};
        //int[][] input_state = {{7, 2, 4}, {5, 0,6}, {8,3,1}};
        //int[][] goal_state = {{1, 2, 3}, {4, 5,6}, {7, 8,0}};
        int choice = -1;

        while (choice != 0) {
            visited.clear();
            statesToBeExpanded.clear();
            nodeGenerated = 0;
            System.out.println("8-puzzle problem");
            System.out.println("Choose heuristic function to solve the puzzle");
            System.out.println("1.Manhattan Distance");
            System.out.println("2.Misplaced Tiles");
            System.out.println("0.Exit");
            Scanner scan = new Scanner(System.in);
            choice = scan.nextInt();
            if (choice == 0)
                System.exit(0);
            if (choice != 1 && choice != 2 && choice != 0) {
                System.out.println("Invalid choice of heuristic function. Please select correct heuristic function and try again!");
                System.exit(0);
            }
            //int[][] input_state = {{1, 2, 3}, {4, 8, 0}, {7, 6, 5}};
            //int[][] goal_state = {{1, 2, 3}, {4, 5,6}, {7, 8, 0}};

            int[][] input_state = null, goal_state = null;

            try {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

                System.out.println("Provide input state in the form {{x,x,x},{x,x,x},{x,x,x}} using digits 0 to 8");
                String inputString = br.readLine();
                input_state = Util.convertStringTo2DArray(inputString.trim());

                System.out.println("Provide goal state in the form {{x,x,x},{x,x,x},{x,x,x}} using digits 0 to 8");
                String goalString = br.readLine();
                goal_state = Util.convertStringTo2DArray(goalString.trim());
            } catch (Exception ex) {
                System.out.println("Error reading user input, provide input again");
                System.exit(0);
            }

            System.out.println("Input state is: ");
            Util.printMat(input_state);
            System.out.println("Goal state is: ");
            Util.printMat(goal_state);
            solve8PuzzleProblem(input_state, goal_state, choice);
        }
    }

    private static void solve8PuzzleProblem(int[][] input_state, int[][] goal_state, int heuristic) {
        int g = 0;
        int f = 0;
        int h = 0;
        h = findHeuristicValue(input_state, goal_state, heuristic);

        State inputState = new State(Util.copyMat(input_state), g, h, (g + h));
        statesToBeExpanded.add(inputState);
        boolean goalReached = false;
        ArrayList<String> path = new ArrayList<>();
        ArrayList<State> statePath = new ArrayList<>();
        while (!statesToBeExpanded.isEmpty()) {
            State polledState = statesToBeExpanded.poll();
            if (debug) {
                System.out.println("Polled state is : ");
                System.out.println(polledState.toString());
            }
            if (polledState.getH() == 0) {
                //we have found the goal state, so break the loop

                statePath.addAll(polledState.getStatePath());
                statePath.add(polledState);
                goalReached = true;
                break;
            } else {
                visited.add(Util.matToString(polledState.getState()));
                ArrayList<int[][]> nextPossibleStateList = findNextState(polledState.getState());
                if (debug) {
                    System.out.println("There are " + nextPossibleStateList.size() + " possible next states for this state");
                }
                for (int[][] nextState : nextPossibleStateList) {
                    if (debug) {
                        Util.printMat(nextState);
                    }
                    h = findHeuristicValue(nextState, goal_state, heuristic);
                    g = polledState.getG() + 1;
                    f = h + g;
                    if (debug) {
                        System.out.println("g: " + g + " h: " + h + " f:" + f);
                        System.out.println();
                    }
                    State s = new State(nextState, g, h, f);

                    s.getStatePath().addAll(polledState.getStatePath());
                    s.getStatePath().add(polledState);
                    statesToBeExpanded.add(s);
                    nodeGenerated++;
                }
            }
        }
        if (goalReached) {
            System.out.println("goal state found");
            System.out.println("Nodes Generated : " + nodeGenerated);
            System.out.println("Nodes expanded : " + visited.size());
            System.out.println("Path cost : " + (statePath.size()-1));
            System.out.println("Path :");
            printPath(statePath);
        } else {
            System.out.println("goal state not found");
        }
    }

    private static void printPath(ArrayList<State> pathList) {
        for(State state: pathList){
                //Util.printMat(Util.stringToMatrix(state));
                state.toString();
                System.out.println("------------------------------------------------------");
        }
    }
    /*private static void printPath(ArrayList<String> pathList) {
        for(String state: pathList){
            try {
                Util.printMat(Util.stringToMatrix(state));
                System.out.println("------------------------------------------------------");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }*/

    private static int findHeuristicValue(int[][] input_state, int[][] goal_state, int heuristic) {
        int dist = -1;
        if (heuristic == 1)
            dist = manhattanDistance(input_state, goal_state);
        else if (heuristic == 2)
            dist = misplacedTiles(input_state, goal_state);
        return dist;
    }

    private static ArrayList<int[][]> findNextState(int[][] input_state) {
        ArrayList<int[][]> list = new ArrayList<int[][]>();

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (input_state[i][j] == 0) {
                    if (i + 1 < 3) {
                        int[][] nextstate = Util.copyMat(input_state);
                        int temp = nextstate[i + 1][j];
                        nextstate[i + 1][j] = nextstate[i][j];
                        nextstate[i][j] = temp;
                        if (!visited.contains(Util.matToString(nextstate)))
                            list.add(nextstate);
                    }
                    if (i - 1 >= 0) {
                        int[][] nextstate = Util.copyMat(input_state);
                        int temp = nextstate[i - 1][j];
                        nextstate[i - 1][j] = nextstate[i][j];
                        nextstate[i][j] = temp;
                        if (!visited.contains(Util.matToString(nextstate)))
                            list.add(nextstate);
                    }
                    if (j + 1 < 3) {
                        int[][] nextstate = Util.copyMat(input_state);
                        int temp = nextstate[i][j + 1];
                        nextstate[i][j + 1] = nextstate[i][j];
                        nextstate[i][j] = temp;
                        if (!visited.contains(Util.matToString(nextstate)))
                            list.add(nextstate);
                    }
                    if (j - 1 >= 0) {
                        int[][] nextstate = Util.copyMat(input_state);
                        int temp = nextstate[i][j - 1];
                        nextstate[i][j - 1] = nextstate[i][j];
                        nextstate[i][j] = temp;
                        if (!visited.contains(Util.matToString(nextstate)))
                            list.add(nextstate);
                    }
                    return list;
                }
            }
        }

        return null;
    }

    private static int manhattanDistance(int[][] input_state, int[][] goal_state) {
        int dist = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (input_state[i][j] != goal_state[i][j]) {
                    dist += findInversion(input_state[i][j], i, j, goal_state);
                    //System.out.println("Manhattan dist of "+input_state[i][j]+" :" + dist);
                }
            }
        }
        return dist;
    }

    private static int misplacedTiles(int[][] input_state, int[][] goal_state) {
        int misplacedTiles = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (input_state[i][j] != goal_state[i][j]) {
                    misplacedTiles += 1;
                }
            }
        }
        return misplacedTiles;
    }

    private static int findInversion(int num, int indexi, int indexj, int[][] goal_state) {
        int inv = 0;
        if (num == 0) return 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {

                if (num == goal_state[i][j]) {
                    inv = Math.abs(indexi - i) + Math.abs(indexj - j);
                    //System.out.println("inv "+input_state[indexi][indexj]+" :" + inv);
                    return inv;
                }
            }
        }
        return 0;
    }
}
