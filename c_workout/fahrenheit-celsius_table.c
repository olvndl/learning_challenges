# include <stdio.h>

int main() {
    int fahr, celsius;
    int upper, step;

    upper = 300;
    step = 20;

    fahr = 0;

    while (fahr <= upper) {
        celsius = 5 * (fahr-32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr += step;
    }
}