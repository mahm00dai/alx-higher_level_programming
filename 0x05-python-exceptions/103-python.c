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
	PyListObject *list_obj;

	if (!PyList_Check(p))
	{
		printf("[.] Invalid List Object\n");
		return;
	}

	list_obj = (PyListObject *)p;
	size = list_obj->ob_base.ob_size;
	allocated = list_obj->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = list_obj->ob_item[i];
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
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
	PyBytesObject *bytes_obj;

	if (!PyBytes_Check(p))
	{
		printf("[.] Invalid Bytes Object\n");
		return;
	}

	bytes_obj = (PyBytesObject *)p;
	size = bytes_obj->ob_base.ob_size;
	str = (const char *)bytes_obj->ob_sval;

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
	PyFloatObject *float_obj;

	if (!PyFloat_Check(p))
	{
		printf("[.] Invalid Float Object\n");
		return;
	}

	float_obj = (PyFloatObject *)p;
	printf("[.] float object info\n");
	printf("  value: %f\n", float_obj->ob_fval);
}

