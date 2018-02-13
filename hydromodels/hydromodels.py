import numpy as np

from cffi import FFI
from hydromodels import _hydromodels_cffi
import logging
logger = logging.getLogger(__name__)

class GR4J():
    __ffi = FFI()
    __lib = _hydromodels_cffi.lib
    def __init__(self, params):
        self.__ptr = self.__lib.gr4j_init(
            params['X1'],
            params['X2'],
            params['X3'],
            params['X4']
        )

    def run(self, precip, pet):
        assert len(precip) == len(pet)
        if precip.dtype != np.float64:
            logger.warn("Precipitation series not float64, conversion may result in copy")
            precip = precip.astype(np.float64, copy = False)

        if pet.dtype != np.float64:
            logger.warn("PET series not float64, conversion may result in copy")
            pet = pet.astype(np.float64, copy = False)

        qsim = np.empty_like(precip, dtype=np.float64)
        qsim[:] = np.nan

        self.__lib.gr4j_run(
            self.__ptr,
            self.__ffi.cast('double *', precip.ctypes.data),
            self.__ffi.cast('double *', pet.ctypes.data),
            self.__ffi.cast('double *', qsim.ctypes.data),
            self.__ffi.cast('int', len(precip))
        )

        return qsim

    def __str__(self):
        return str(self.__ptr)

    def __del__(self):
        self.__lib.gr4j_destroy(self.__ptr)
