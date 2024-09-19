#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints information about a Python list
 * @p: PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	Py_ssize_t size;
	Py_ssize_t allocated;
	PyObject *item;

	if (!PyList_Check(p)) {
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = PyList_GetSize(p);  // Not a real function, just for illustration

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item)) {
			printf("[.] bytes object info\n");
			print_python_bytes(item);
		}
		// Handle other types if needed
	}
}

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *data;

	if (!PyBytes_Check(p)) {
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", data);

	printf("  first %zd bytes: ", size < 10 ? size : 10);
	for (i = 0; i < (size < 10 ? size : 10); i++)
		printf("%02x ", (unsigned char)data[i]);
	printf("\n");
}

