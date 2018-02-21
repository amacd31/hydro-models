#include <stdio.h>
#include <Python.h>
#include "numpy/arrayobject.h"

static PyObject *OwndataError;

static PyObject *
owndata_take_ownership(PyObject *self, PyObject *args)
{
    import_array();
    npy_intp *length;
    intptr_t *data_ptr;
    PyArrayObject * data_array;

    if (!PyArg_ParseTuple(args, "ll", &data_ptr, &length))
        return NULL;

    npy_intp dims[1];
    dims[0] = length;
    data_array = (PyArrayObject*)PyArray_SimpleNewFromData(1, dims, NPY_FLOAT64, data_ptr);
    data_array->flags |= NPY_ARRAY_OWNDATA;

    return (PyObject*)data_array;
}

static PyMethodDef OwndataMethods[] = {
    {"take_ownership",  owndata_take_ownership, METH_VARARGS,
    "Take ownership of a C array and return as a numpy array."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef owndatamodule = {
    PyModuleDef_HEAD_INIT,
    "owndata",   /* name of module */
    "", /* module documentation, may be NULL */
    -1,       /* -1 if the module keeps state in global variables. */
    OwndataMethods
};

PyMODINIT_FUNC
PyInit_owndata(void)
{
    import_array();
    PyObject *m;

    m = PyModule_Create(&owndatamodule);
    if (m == NULL) 
        return NULL;

    OwndataError = PyErr_NewException("owndata.error", NULL, NULL);
    Py_INCREF(OwndataError);
    PyModule_AddObject(m, "error", OwndataError);
    return m;
}
