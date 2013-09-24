#include <stdio.h>

int solve_for(int n) {
  printf("Solving for %d\n", n);
  int l[n];
  int i, j;
  for (i = 0; i < n; i++) {
    l[i] = 0;
  }
  for (i = n-1; i >= 0; i--) {
    l[i] = 1;
    for (j = 2*i + 1; j < n; j++) {
      l[j] = (l[j] + l[j - i - 1]) % 1000000;
    }
  }

  for (i = 0; i < n; i++) {
    if (l[i] == 0) {
      return i+1;
    }
  }
  return 0;
}

int main() {
  int m;
  int n = 0;
  for (m = 2; !n; m *= 2) {
    n = solve_for(m);
  }
  printf("%d\n", n);
  return 0;
}
