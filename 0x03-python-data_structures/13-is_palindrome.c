#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

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
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		second_half = slow->next;
		slow->next = prev;
	}
	else
	{
		second_half = slow;
		prev->next = NULL;
	}
	while (second_half != NULL)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}
	second_half = prev;
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
		is_palindrome = 0;
		break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	return (is_palindrome);
}
