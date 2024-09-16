package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

func convertToMinutes(time string) int {
	parts := strings.Split(time, ":")
	hours, _ := strconv.Atoi(parts[0])
	minutes, _ := strconv.Atoi(parts[1])
	return hours*60 + minutes
}

func findMinDifference(timePoints []string) int {
	// Convert all time strings to minutes
	minutes := make([]int, len(timePoints))
	for i, time := range timePoints {
		minutes[i] = convertToMinutes(time)
	}

	// Sort the time points in ascending order
	sort.Ints(minutes)

	// Initialize the minimum difference to a large number
	minDiff := math.MaxInt32

	// Calculate the minimum difference between consecutive time points
	for i := 1; i < len(minutes); i++ {
		diff := minutes[i] - minutes[i-1]
		if diff < minDiff {
			minDiff = diff
		}
	}

	// Check the difference between the first and last time points (wrap-around case)
	wrapAroundDiff := 1440 - minutes[len(minutes)-1] + minutes[0]
	if wrapAroundDiff < minDiff {
		minDiff = wrapAroundDiff
	}

	return minDiff
}