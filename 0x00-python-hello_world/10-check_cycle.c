#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list.
 * @list: a pointer to the list to be checked.
 *
 * Return: 0 if there is not a cycle; 1 if a cycle is found.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	if (list == NULL || list->next == NULL)
		return (0);

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
