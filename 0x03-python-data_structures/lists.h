#ifndef LISTS_H
#define LISTS_H

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * * Description: structures
 * @n: the n value
 * struct listint_s - list the items
 * @next: poit to the next data

 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);
void reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
size_t print_listint(const listint_t *h);

#endif
