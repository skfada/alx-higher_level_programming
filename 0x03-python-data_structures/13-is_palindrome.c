#include "lists.h"

/**
 * Return: none
 * reverse - the preevious
 * @h_r: pointerv to pointer
 */
void reverse(listint_t **h_r)
{
	listint_t *next;
	listint_t *prev;
	listint_t *curr;

	prev = NULL;
	curr = *h_r;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*h_r = prev;
}

/**
 * * Return: hthe
 * compare - hjkk
 * @h1: head1
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp2;
	listint_t *tmp1;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * * Return: 1 or 0
 * is_palindrome - hth
 * @head: the head
 */
int is_palindrome(listint_t **head)
{
	int isp;
	listint_t *scn_half, *middle;
	listint_t *slow, *fast, *prev_slow;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
