#[macro_use]
extern crate cpython;

use cpython::{Python, PyResult};


fn print_from_rs(_: Python) -> PyResult<u64> {

    const VERSION: &'static str = env!("CARGO_PKG_VERSION");
    println!("PyRust version : {}", VERSION);
    Ok(1)
}

fn count_doubles(_: Python, val: &str) -> PyResult<u64> {
    let mut total = 0u64;

    for (c1, c2) in val.chars().zip(val.chars().skip(1)) {
        if c1 == c2 {
            total += 1;
        }
    }
    
    Ok(total)
}

fn search_text(_: Python, target: &str, val: &str) -> PyResult<u64> {
    let mut total = 0u64;
    let iter = val.split_whitespace();
    for word in iter {
        match word == target {
            true => total += 1,
            false => {}
        }
    }
    
    Ok(total)
}

fn sum_list(_: Python, list: Vec<u64>) -> PyResult<u64> {
    let mut total = 0u64;

    for num in list {
        total += num
    }

    Ok(total)
}


py_module_initializer!(libpyrust, initlibpyrust, PyInit_libpyrust, |py, m| {
    try!(m.add(py, "__doc__", "This module is implemented in Rust."));
    try!(m.add(py, "print_from_rs", py_fn!(py, print_from_rs())));
    try!(m.add(py, "count_doubles", py_fn!(py, count_doubles(val: &str))));
    try!(m.add(py, "search_text", py_fn!(py, search_text(target: &str, val: &str))));
    try!(m.add(py, "sum_list", py_fn!(py, sum_list(list: Vec<u64>))));
    Ok(())
});
