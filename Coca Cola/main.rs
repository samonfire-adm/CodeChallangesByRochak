fn cococola(n: i32) {
    for i in 1..=n {
        if i % 3 == 0 && i % 5 == 0 {
            println!("CocoCola");
        } else if i % 3 == 0 {
            println!("Coca");
        } else if i % 5 == 0 {
            println!("Cola");
        } else {
            println!("{}", i);
        }
    }
}

fn main() {
    cococola(15);
}
