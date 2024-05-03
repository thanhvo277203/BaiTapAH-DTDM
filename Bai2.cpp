#include <stdio.h>
#include <math.h>

// Ham kiem tra so chinh phuong
int isPerfectSquare(int num) {
    int squareRoot = sqrt(num);
    return squareRoot * squareRoot == num;
}

// Ham dem va in ra cac so chinh phuong nho hon n
void countAndPrintPerfectSquares(int n) {
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d, ", i);
            count++;
        }
    }
    printf("\nTong so chinh phuong: %d\n", count);
}

int main() {
    int n;
    printf("Nhap so nguyen duong n: ");
    scanf_s("%d", &n);
    countAndPrintPerfectSquares(n);
    return 0;
}
