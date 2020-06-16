package com.company;

import java.util.ArrayList;
import java.util.Arrays;

public class State implements Comparable<State> {
    private int[][] state;
    private int h;
    private int g;
    private int f;
    private ArrayList<State> statePath;

    public State(int[][] state, int g, int h, int f) {
        this.state = state;
        this.h = h;
        this.g = g;
        this.f = f;
        this.statePath = new ArrayList<>();
    }

    @Override
    public int compareTo(State o) {
        if(this.f>o.f) return 1;
        else if(this.f<o.f) return -1;
        else return 0;
    }

    @Override
    public String toString() {
        for (int i = 0; i < 3; i++) {
            System.out.print("\t");
            for (int j = 0; j < 3; j++) {
                System.out.print(state[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("g:" + g + "\th:" + h +"\tf:" + f);

        return "";
    }

    public int[][] getState() {
        return state;
    }

    public void setState(int[][] state) {
        this.state = state;
    }

    public int getH() {
        return h;
    }

    public void setH(int h) {
        this.h = h;
    }

    public int getG() {
        return g;
    }

    public void setG(int g) {
        this.g = g;
    }

    public int getF() {
        return f;
    }

    public void setF(int f) {
        this.f = f;
    }

    public ArrayList<State> getStatePath() {
        return statePath;
    }

    public void setStatePath(ArrayList<State> statePath) {
        this.statePath = statePath;
    }
}
