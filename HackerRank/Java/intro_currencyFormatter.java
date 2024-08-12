// https://www.hackerrank.com/challenges/java-currency-formatter
// Difficulty: EASY

import java.util.*;
import java.text.*;

public class intro_currencyFormatter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        NumberFormat us = NumberFormat.getInstance(Locale.US);
        
        // some manual controls because the HackerRank compiler is erratic
        // DecimalFormatSymbols dfs = new DecimalFormatSymbols();
        // dfs.setCurrencySymbol("$");
        // dfs.setGroupingSeparator(',');
        // dfs.setMonetaryDecimalSeparator('.');
        // ((DecimalFormat) us).setDecimalFormatSymbols(dfs);
        us.setMinimumFractionDigits(2);
        us.setMaximumFractionDigits(2);
        
        NumberFormat india = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        NumberFormat china = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        
        System.out.println("US: $" + us.format(payment));
        System.out.println("India: " + india.format(payment));
        System.out.println("China: " + china.format(payment));
        System.out.println("France: " + france.format(payment));
    }
}