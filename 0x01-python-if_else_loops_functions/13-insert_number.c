#include "lists.h"
/**
 * insert_node - new node
 * Return: adrssd
 * @number: number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *headCopy;
	listint_t *h_prev;

	headCopy = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (headCopy != NULL)
	{
		if (headCopy->n > number)
			break;
		h_prev = headCopy;
		headCopy = headCopy->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = headCopy;
		if (headCopy == *head)
			*head = new;
		else
			h_prev->next = new;
	}

	return (new);
}
