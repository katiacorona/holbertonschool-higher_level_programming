#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list.
 * @list: a pointer to the list to be checked.
 *
 * Return: 0 if there is not a cycle; 1 if a cycle is found.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = hare = list;
	while (hare && turtle)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (hare == turtle)
			return (1);
	}
	return (0);
}
