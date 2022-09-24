#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - shows info about Python lists
 * @p: object
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int listof, a, i;

	i = 0;
	PyObject *obj;

	listof = Pylistof(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", listof);
	printf("[*] Allocated = %ld\n", a);
	while (i < listof)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
