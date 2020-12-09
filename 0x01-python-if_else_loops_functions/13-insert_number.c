#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a singly linked list
 * @head: double pointer
 * @number: int
 * Return: yes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *nextnode;

	nextnode = malloc(sizeof(listint_t));
	if (!nextnode)
		return (NULL);
	nextnode->n = number;
	if (*head == NULL)
	{
		*head = nextnode;
		nextnode->next = NULL;
		return (nextnode);
	}
	if ((*head)->n > number)
	{
		nextnode->next = *head;
		*head = nextnode;
		return (nextnode);
	}
/*	for (i = 0; node->next->n < number; node = node->next) */
	while (node->next != NULL)
	{
		if (number < node->next->n)
			break;
		else
			node = node->next;
	}
	nextnode->next = node->next;
	node->next = nextnode;
	return (nextnode);
}
