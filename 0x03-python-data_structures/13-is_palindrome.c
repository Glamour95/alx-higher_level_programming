#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to pointer to the head of the list
 *
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		mid = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	second_half = slow;
	mid->next = NULL;
	reverse_listint(&second_half);

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}

	return (1);
}
