#include <stdio.h>

int binary_search(int arr[], int arr_size, int target) {
    if (arr_size == 0) {
        return -1; // handle empty array case
    }

    size_t low_index = 0;
    size_t high_index = arr_size - 1;

    while (low_index <= high_index) {
        size_t mid_index = (low_index + high_index) / 2;

        if (arr[mid_index] == target) {
            return mid_index;
        }
        else if (arr[mid_index] < target) {
            low_index = mid_index + 1;
        }
        else {
            high_index = mid_index - 1;
        }
    }

    return -1;
}


int main() {
    int arr[7] = {1, 2, 4, 5, 7, 8, 9};
    size_t size = 7;
    int target = 5;

    int res = binary_search(arr, size, target);

    if (res == -1) {
        printf("Target not found\n");
    }
    else {
        printf("Element %d stored in index %d\n", target, res);
    }
    return 0;
}