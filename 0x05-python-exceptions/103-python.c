#include <Python.h>

/* Function prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a PyObject representing a Python list
 *
 * If p is not a valid PyListObject, an error message is printed.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[.] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i); /* Get item without error checking */
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 *
 * If p is not a valid PyBytesObject, an error message is printed.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	const char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str ? str : "(null)");
	printf("  first %zd bytes: ", size < 10 ? size : 10);
	for (i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < (size < 10 ? size : 10) - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a PyObject representing a Python float object
 *
 * If p is not a valid PyFloatObject, an error message is printed.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AsDouble(p));
}

