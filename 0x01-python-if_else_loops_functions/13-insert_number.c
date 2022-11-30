#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node at a given point in listint
 * @head: pointer to pointer of head of node
 * @number: int value in node
 *
 * Return: address of new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;
	listint_t *current;

	current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	while (current->next->n < number)
	{
		current = current->next;
	}
	temp = current->next;
	current->next = new_node;
	new_node->next = temp;

	return (new_node);
}

