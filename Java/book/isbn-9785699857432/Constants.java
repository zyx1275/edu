public class Constants {
    public static void main(String[] args) {
        final int TOUCHDOWN = 6;
        final int CONVERSION = 1;
        final int FILEGOAL = 3;

        int td, pat, fg, total;

        td = 4 * TOUCHDOWN;
        pat = 3 * CONVERSION;
        fg = 2 * FILEGOAL;
        total = (td + pat + fg);

        System.out.println("Всего очков: " + total);
    }
}
