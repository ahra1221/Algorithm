class Solution {

    int[][] books;
    int shelfWidth;
    int[] shelf;

    public int minHeightShelves(int[][] books, int shelfWidth) {
        this.books = books;
        this.shelfWidth = shelfWidth;
        shelf = new int[books.length];
        Arrays.fill(shelf, -1);

        return dp(0);
    }

    int dp(int n) {
        if(n == books.length) {
            return 0;
        }

        if(shelf[n] != -1) {
            return shelf[n];
        }

        int width = 0;
        int height = 0;
        int res = Integer.MAX_VALUE;
        for(int i=n;i<books.length;i++) {
            int w = books[i][0];
            int h = books[i][1];

            width += w;
            if(width > shelfWidth) {
                break;
            }
            height = Math.max(height, h);
            res = Math.min(res, height+ dp(i+1));
        }
        shelf[n] = res;
        return res;
    }
}