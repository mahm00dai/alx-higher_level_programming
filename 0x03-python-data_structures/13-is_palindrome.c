#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
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
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *first_half;
	listint_t *copy_of_second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* Reverse the second half */
	second_half = slow;
	copy_of_second_half = reverse_list(&second_half);
	first_half = *head;

	/* Compare the first half with the reversed second half */
	while (copy_of_second_half != NULL)
	{
		if (first_half->n != copy_of_second_half->n)
		{
			/* Restore the list and return 0 */
			reverse_list(&second_half);
			return (0);
		}
		first_half = first_half->next;
		copy_of_second_half = copy_of_second_half->next;
	}

	/* Restore the original list */
	reverse_list(&second_half);

	return (1);
}

