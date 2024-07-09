#!/usr/bin/python3
# Function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def find_peak_util(arr, low, high, n):
        mid = (low + high) // 2

        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1, n)
        else:
            return find_peak_util(arr, mid + 1, high, n)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1, len(list_of_integers))