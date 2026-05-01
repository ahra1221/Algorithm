class Solution {

    public boolean check_dist(String[] place, int x, int y) {
        int[][] oneDir = {{1,0},{0,1}};
        int[][] twoDir = {{2,0},{0,2}};
        int[][] crossDir = {{1,1},{1,-1}};
        
        for(int[] dir: oneDir) {
            int nx = x+dir[0], ny = y+dir[1];
            if(0<=nx && nx<5 && 0<=ny && ny<5) {
                if (place[nx].charAt(ny) == 'P') return false;
            }
        }
        
        for(int[] dir: crossDir) {
            int nx = x+dir[0], ny = y+dir[1];
            if(0<=nx && nx<5 && 0<=ny && ny<5 && place[nx].charAt(ny) == 'P') {
                if (!(place[nx].charAt(y) == 'X' && place[x].charAt(ny) == 'X')) {
                    return false;
                }
            }
        }
        
        int tmp = 0;
        for(int[] dir: twoDir) {
            int nx = x+dir[0], ny = y+dir[1];
            if(0<=nx && nx<5 && 0<=ny && ny<5 && place[nx].charAt(ny) == 'P') {
                if(place[x+oneDir[tmp][0]].charAt(y+oneDir[tmp][1]) != 'X') return false;
            }
            tmp++;
        }
        
        return true;
    }    
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        
        for(int p=0;p<5;p++) {
            boolean flag = true;
            for(int i=0;i<5;i++) {
                int j = 0;
                for(char c: places[p][i].toCharArray()) {
                    if (c == 'P') {
                        if (!check_dist(places[p], i, j)) {
                            flag = false;
                            break;
                        }
                    }
                    j++;
                }
                if (!flag) break;
            }
            answer[p] = flag ? 1 : 0;
        }
        
        return answer;
    }
}