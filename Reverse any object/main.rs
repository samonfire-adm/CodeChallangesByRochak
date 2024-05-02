fn reverse_string(input_string: &str) -> String {
    let mut stack: Vec<char> = Vec::new();
    for char in input_string.chars() {
        stack.push(char);
    }

    let mut reversed_string = String::new();
    while let Some(char) = stack.pop() {
        reversed_string.push(char);
    }
    reversed_string
}
fn main() {
    let input_string = "Hello, world!";
    let reversed_string = reverse_string(input_string);
    println!("Original string: {}", input_string);
    println!("Reversed string: {}", reversed_string);
}
