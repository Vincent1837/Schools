#include <stdio.h>
#include <limits.h>

// Utility function to find the maximum of two integers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Recursive function to find the maximum profit from rod cutting
int rodCutting(int price[], int n) {
    // Base case: If the rod length is 0, the profit is 0
    if (n == 0)
        return 0;

    int maxProfit = INT_MIN;

    // Try cutting the rod into different lengths and recursively find the maximum profit
    for (int i = 1; i <= n; i++) {
        maxProfit = max(maxProfit, price[i - 1] + rodCutting(price, n - i));
    }

    return maxProfit;
}

int rod_cutting(int n, int prices[], int cut_cost) {
    int dp[n+1]; // Array to store the maximum revenue for each rod length
    dp[0] = 0; // Base case
    for (int i = 1; i <= n; i++) {
        int max_revenue = INT_MIN; // Initialize max revenue for rod length i
        // Try all possible cuts for rod length i
        for (int j = 1; j <= i; j++) {
            int revenue = prices[j] + dp[i - j] - ((j != i) ? cut_cost : 0);
            max_revenue = max(max_revenue, revenue);
        }
        dp[i] = max_revenue;
    }
    return dp[n];
}

int main() {
    int prices[] = {0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    int cut_cost = 0;
    int rod_length = 9;

    int max_revenue = rod_cutting(rod_length, prices, cut_cost);
    printf("Maximum revenue: %d\n", max_revenue);

    return 0;
}
