from cffi import FFI

ffi = FFI()

ffi.cdef(
"""
void* gr4j_init(double x1, double x2, double x3, double x4);
void* gr4j_run(double * ptr, double * precip, double * pet, double * qsim_ptr, int n);
void* gr4j_destroy(double * ptr);
"""
)

ffi.set_source(
    "hydromodels._hydromodels_cffi",
    """
    void* gr4j_init(double x1, double x2, double x3, double x4);
    void* gr4j_run(double * ptr, double * precip, double * pet, double * qsim_ptr, int n);
    void* gr4j_destroy(double * ptr);
    """,
    libraries = ['hydromodels_interface'],
    library_dirs = ['/Users/amacdon/code/hydro-models/target/debug'],
)


if __name__ == '__main__':
    ffi.compile()
