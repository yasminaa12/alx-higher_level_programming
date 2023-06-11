#include "lists.h"

/**
 * reverse_listint - reverses linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *cur = *head;
	listint_t *nxt = NULL;

	while (cur)
	{
		nxt = cur->next;
		cur->next = prv;
		prv = cur;
		cur = nxt;
	}
	*head = prv;
}

/**
 * is_palindrome - checks if linked list is palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *tmp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			dup = s->next;
			break;
		}
		if (!f->next)
		{
			dup = s->next->next;
			break;
		}
		s = s->next;
	}
	reverse_listint(&dup);
	while (dup && tmp)
	{
		if (tmp->n == dup->n)
		{
			dup = dup->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	return (0);
}
