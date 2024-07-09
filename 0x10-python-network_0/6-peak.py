#!/usr/bin/python3
# Function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    """Function to find the peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size ==0:
        return (None)
    elif size == 0:
        return (list_of_integers[0])
    elif size == 1:
        return max(list_of_integers)
    mid = int(size/2)
    peak = list_of_integers[mid]
    list = list_of_integers
    if peak > list[mid - 1] and peak > list[mid + 1]:
        return peak
    elif peak < list[mid -1]:
        return find_peak(list[:mid])
    else:
        return find_peak(list[mid + 1:])
