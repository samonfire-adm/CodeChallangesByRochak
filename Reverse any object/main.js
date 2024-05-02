function reverseString(inputString) {
    const stack = [];
    for (const char of inputString) {
        stack.push(char);
    }
    let reversedString = '';
    while (stack.length > 0) {
        reversedString += stack.pop();
    }
    return reversedString;
}

const inputString = "Hello, world!";
const reversedString = reverseString(inputString);
console.log("Original string:", inputString);
console.log("Reversed string:", reversedString);
