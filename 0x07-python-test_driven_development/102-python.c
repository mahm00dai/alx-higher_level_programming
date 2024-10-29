#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A pointer to a Python object.
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	/* Check if p is a Unicode object */
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Get the type of string encoding (ASCII or Unicode) */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	/* Get the length of the string */
	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	
	printf("  length: %ld\n", length);

	/* Get the value of the string */
	const char *value = PyUnicode_AsUTF8(p);

	printf("  value: %s\n", value);
}

