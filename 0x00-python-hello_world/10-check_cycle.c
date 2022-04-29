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

	turtle = list->next;
	hare = list->next->next;
	while (turtle != NULL && hare != NULL && hare->next != NULL)
	{
		if (turtle == hare)
			return (1);
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}
