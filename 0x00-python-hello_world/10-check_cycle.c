#include "lists.h"

/**
 * check_cycle - checks if singly linked list has cycle in it
 * @list: pointer to beginning of node
 * Return: 0: no cycle, 1: there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cur, *chk;

	if (list == NULL || list->next == NULL)
		return (0);
	cur = list;
	chk = cur->next;
	while (cur != NULL && chk->next != NULL
		&& chk->next->next != NULL)
	{
		if (cur == chk)
			return (1);
		cur = cur->next;
		chk = chk->next->next;
	}
	return (0);
}
