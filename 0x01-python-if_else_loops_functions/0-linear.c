#include <stdio.h>
#include "search_algos.h"

/**
 * Function that searches for a value in an array of integers
 * Using the Linear search algorithm
 * @array: Pointer to the first element of the array to search in
 * @size: Is the number of elements in array
 * @value: Value to search for
 * Return: If value is not present in array or if array is NULL,
 * your function must return -1
 */
int linear_search(int *array, size_t size, int value)
{
    size_t i;

    if (array == NULL)
        return (-1);

    for (i = 0; i < size; i++)
    {
        printf("Value checked array[%lu] = [%d]\n", i, array[i]);
        if (array[i] == value)
            return (i);
    }

    return (-1);
}

