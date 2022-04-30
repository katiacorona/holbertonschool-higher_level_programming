#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Inserts a node in a sorted linked list.
 *
 * @head: a Pointer to the first node of the list.
 * @number: The data to be stored in the newly inserted node.
 *
 * Return: The address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *back, *front, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	front = *head;
	if (front->next == NULL)
	{
		*head = new;
		return (new);
	}

	back = NULL;
	while (front && front->n < number)
	{
		back = front;
		front = front->next;
	}
	back->next = new;
	new->next = front;
	return (new);
}
