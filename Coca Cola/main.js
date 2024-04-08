function cococola(n) {
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log("CocoCola");
        } else if (i % 3 === 0) {
            console.log("Coca");
        } else if (i % 5 === 0) {
            console.log("Cola");
        } else {
            console.log(i);
        }
    }
}

cococola(15);
