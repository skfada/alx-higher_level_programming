#include "lists.h"
/**
 * Return: 0 if there is no cycle
 * check_cycle - checks if a singly linked list has
 * @list: pointer to the list 
 */
int check_cycle(listint_t *list)
{
  listint_t *prev;
	listint_t *py;	

	py = list;
	prev = list;
	while (list && py && py->next)
	{
		list = list->next;
		py = py->next->next;

		if (list == py)
		{
			list = prev;
			prev =  py;
			while (1)
			{
				py = prev;
				while (py->next != list && py->next != prev)
				{
					py = py->next;
				}
				if (py->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
