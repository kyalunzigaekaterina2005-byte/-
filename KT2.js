// Задание 1
let word = 'Арнольд';
let result = '';

for (let i = 0; i < word.length; i++) {
    let n = word[i].toLowerCase();
    if (n !== 'а' && n !== 'о') {
        result += word[i];
    }
}

console.log(result);

// Задача 2
let num = 20;
for (let i = 1; i <= num; i++) {
    if (i % 3 === 0) {
        console.log(i);
    }
}

// Задача 3
let num2 = 5;
let result2 = '';

for (let i = 1; i <= num2; i++) {
    result2 += i;
    console.log(result2);
}

// Задача 4
let num3 = 4;
let sum = 0;
let factorial = 1;

for (let i = 1; i <= num3; i++) {
    factorial = factorial * i;
    sum = sum + factorial;
}

console.log(sum);

// Задача 5
let word2 = 'потоп';
let palindrome = '';

for (let i = word2.length - 1; i >= 0; i--) {
    palindrome += word2[i];
}

if (word2 === palindrome) {
    console.log('YES');
}
else {
    console.log('NO');
}
