#include "lists.h"

/**
 * insert_node - Entry point
 * @head: A pointer
 * @number: num insert
 * Return: 0 always
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *js = *head, *new;

	new = malloc(sizeof(listint_t));
	
	if (new == NULL)
		return (NULL);
	
	new->n = number;

	if (js == NULL || js->n >= number)
	{
		new->next = js;
		*head = new;
		return (new);
	}

	while (js && js->next && js->next->n < number)
		js = js->next;

	new->next = js->next;
	
	js->next = new;

	return (new);
}
