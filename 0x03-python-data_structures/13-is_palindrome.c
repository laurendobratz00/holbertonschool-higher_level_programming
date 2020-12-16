#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: double pointer
 * Return: yes
 */

int is_palindrome(listint_t **head)
{
	int name[1024], val, i, j;
	listint_t *itr;

	if (*head == NULL)
		return (1);

	itr = *head;

	for (i = 0; i < 1024; i++)
		name[i] = 0;
	for (i = 0;


}
