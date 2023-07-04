#include <Python.h>
#include <unicodeobject.h>
#include <object.h>


void print_python_string(PyObject *p)
{
    wchar_t *str = NULL;
    const char *type = NULL;
    Py_ssize_t len = 0;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        type = "compact ascii";
    else
        type = "compact unicode object";

    str = PyUnicode_AsWideCharString(p, &len);

    printf("  type: %s\n", type);
    printf("  length: %ld\n", len);
    printf("  value: %ls\n", str);
}
