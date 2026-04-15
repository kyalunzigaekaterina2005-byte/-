// Задача 1
function checkElem(num) {
    if (num % 7 === 0) {
        console.log(true);
    }
    else {
        console.log(false);
    }
}

checkElem(13);
checkElem(14);

// Задача 2
function changeElem(array, n) {
    return array.map(array => array * n);
}

let array2 = [1, 2, 3, 4]
let result2 = changeElem(array2, 3)
console.log(result2)

// Задача 3
function sumElems(array) {
    let sum = 0;
    for (let str of array) {
        let num = Number(str);
        if (!isNaN(num)) {
            sum += num;
        }
    }
    return sum;
}

let array3 = ['10','Строка','5g','15','05']
let result3 = sumElems(array3)
console.log(result3)

// Задача 4
function reverseIndex(array) {
    let newArray = [];
    for (let i = array.length - 1; i >= 0; i--) {
        newArray.push(array[i]);
    }
    console.log(newArray)
}

let array4 = [1, 2, 3, 4, 5]
reverseIndex(array4)

// Задача 5
function checkElem2(array, callback) {
    for(let elem of array) {
        if (callback(elem)) {
            return true;
        }
    }
    return false;
}

let array5 = [1, 2, 3, 4];
let result5 = checkElem2(array5, (elem) => elem == 3);
console.log(result5)
