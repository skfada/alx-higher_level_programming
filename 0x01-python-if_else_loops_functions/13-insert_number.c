#include "lists.h"
/**
 * @head: head of a list.
 * @number: index of the list where the new node is
 * insert_node - inserts a new node
 * Return: the address of the new node, or NULL if it
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *head_prev;
	listint_t *head;
    listint_t *new;	

	head = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (head != NULL)
	{
		if (head->n > number)
			break;
		head_prev = head;
		head = head->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = head;
		if (head == *head)
			*head = new;
		else
			head_prev->next = new;
	}

	return (new);
}
