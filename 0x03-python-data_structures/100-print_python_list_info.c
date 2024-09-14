#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list object
 * @p: The Python list object to print information about
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated;
	Py_ssize_t i;
	PyObject *item;

	/* Check if p is a list */
	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Provided object is not a list");
		return;
	}

	size = PyList_Size(p); /* Get the size of the list */
	allocated = ((PyListObject *)p)->allocated; /* Get the allocated size of the list */

	/* Print the size and allocated space */
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	/* Iterate over the list and print the type of each element */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i); /* Get the item at index i */
		if (item == NULL)
		{
			printf("Element %zd: NULL\n", i);
		}
		else
		{
			/* Print the type of the element */
			if (PyUnicode_Check(item))
				printf("Element %zd: str\n", i);
			else if (PyLong_Check(item))
				printf("Element %zd: int\n", i);
			else if (PyFloat_Check(item))
				printf("Element %zd: float\n", i);
			else if (PyTuple_Check(item))
				printf("Element %zd: tuple\n", i);
			else if (PyList_Check(item))
				printf("Element %zd: list\n", i);
			else
				printf("Element %zd: unknown\n", i);
		}
	}
}

