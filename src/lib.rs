extern crate hydromodels;
use std::collections::HashMap;

#[no_mangle]
pub extern "C" fn gr4j_init(x1: f64, x2: f64, x3: f64, x4: f64) -> *mut hydromodels::hydromodels::GR4JModel {
    let mut gr4j = hydromodels::hydromodels::GR4JModel { ..Default::default() };
    let mut params = HashMap::new();
    params.insert("X1", x1);
    params.insert("X2", x2);
    params.insert("X3", x3);
    params.insert("X4", x4);
    gr4j.init(params, None, None, None);
    let ptr = Box::into_raw(Box::new(gr4j));
    ptr
}


#[no_mangle]
pub extern "C" fn gr4j_run(
    model_ptr: *mut hydromodels::hydromodels::GR4JModel,
    precip_ptr: *const f64,
    pet_ptr: *const f64,
    qsim_ptr: *mut f64,
    input_len: usize,
    output_len: usize
) {
    let precip = unsafe { std::slice::from_raw_parts(precip_ptr, input_len) };
    let pet = unsafe { std::slice::from_raw_parts(pet_ptr, input_len) };
    let mut qsim = unsafe { std::slice::from_raw_parts_mut(qsim_ptr, output_len) };

    let mut model = unsafe { Box::from_raw(model_ptr) };

    model.run(precip, pet);

    for i in 0..model.qsim.len() {
        qsim[i] = model.qsim[i];
    }

    // Turn back into raw pointer so that the model isn't cleaned up after a run
    let ptr = Box::into_raw(Box::new(model));
}

#[no_mangle]
pub extern "C" fn gr4j_destroy(model_ptr: *mut f64) {
    let model = unsafe { Box::from_raw(model_ptr) };
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
