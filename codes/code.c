#include <stdio.h>

int main() {
    // Define parameters
    int x[22];
    float y[22];

    // Initialize x values
    for (int i = 0; i < 22; ++i) {
        x[i] = i;
    }

    // Calculate y values
    for (int i = 0; i < 22; ++i) {
        y[i] = 6 + 6 * (i < 22 ? i : 22);
    }

    // Open the file for writing
    FILE *file = fopen("a.dat", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1; // Return with an error code
    }

    // Print x and y values to the file
    for (int i = 0; i < 22; ++i) {
        fprintf(file, "%d %.2f\n", x[i], y[i]);
    }

    // Close the file
    fclose(file);

    return 0; // Return with success code
}
