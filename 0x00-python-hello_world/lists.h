#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * @next: points to the next node
 * struct listint_s - singly linked list
 * Description: singly linked list
 * @n: integer  
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);

#endif
