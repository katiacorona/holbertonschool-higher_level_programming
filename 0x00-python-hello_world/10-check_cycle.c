#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	current = list;
	temp = current->next;
	while (temp->next != NULL)
	{
		if (temp->next == current)
			return (1);
		temp = temp->next;
	}
	return (0);
}
