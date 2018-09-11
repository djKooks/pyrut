cargo build --release

mv target/release/librustring.dylib py/librustring.so
# cd py && pytest test.py -s

