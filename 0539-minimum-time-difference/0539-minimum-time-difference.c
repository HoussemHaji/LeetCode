#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int convertToMinutes(char* time) {
    int hours, minutes;
    sscanf(time, "%d:%d", &hours, &minutes);
    return hours * 60 + minutes;
}

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int findMinDifference(char** timePoints, int timePointsSize) {
    // Convert all time strings to minutes
    int* minutes = (int*)malloc(timePointsSize * sizeof(int));
    
    for (int i = 0; i < timePointsSize; i++) {
        minutes[i] = convertToMinutes(timePoints[i]);
    }
    
    // Sort the time points in ascending order
    qsort(minutes, timePointsSize, sizeof(int), compare);
    
    int minDiff = INT_MAX;
    
    // Calculate the minimum difference between consecutive time points
    for (int i = 1; i < timePointsSize; i++) {
        int diff = minutes[i] - minutes[i - 1];
        if (diff < minDiff) {
            minDiff = diff;
        }
    }
    
    // Check the difference between the first and last time points (wrap-around case)
    int wrapAroundDiff = (1440 - minutes[timePointsSize - 1] + minutes[0]);
    if (wrapAroundDiff < minDiff) {
        minDiff = wrapAroundDiff;
    }
    
    free(minutes);
    
    return minDiff;
}

