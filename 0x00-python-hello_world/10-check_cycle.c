#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @l: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *l)
{
	listint_t *slow = l;
	listint_t *fast = l;

	if (!l)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
