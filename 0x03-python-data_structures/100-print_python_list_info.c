#include <listobject.h>
#include <object.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int index;
	long int size = PyList_Size(p);

	PyListObject *obj = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (index = 0; index < size; index++)
		printf("Element %i: %s\n", index, Py_TYPE(obj->ob_item[index])->tp_name);
}
