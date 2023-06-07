#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;
	if (nd == NULL || nd->n >= number)
	{
		nw->next = nd;
		*head = nw;
		return (nw);
	}
	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;
	nw->next = nd->next;
	nd->next = nw;
	return (nw);
}
