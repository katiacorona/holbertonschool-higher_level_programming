#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *previous, *following, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (head == NULL)
		*head = new;

	previous = *head;
	following = previous->next;
	if (new->n < previous->n)
	{
		*head = new;
		new->next = previous;
	}
	while (previous && following && following->next)
	{
		if (new->n > previous->n && new->n < following->n)
		{
			previous->next = new;
			new->next = following;
			break;
		}
		else if (new->n > following->n)
		{
			previous = previous->next;
			following = following->next;
		}
	}
		
	return (new);
}
