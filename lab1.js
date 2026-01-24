// КТ-1
// Задача 1
price = Number(prompt("Введите сумму дохода"));
range = prompt("Выберите (month, day, week)");
let rus_range;
if (range == "month"){
    rus_range = "месяц"
}
else if (range == "day"){
    rus_range = "день"
}
else if (range == "week"){
    rus_range = "неделю"
}
let result = price + " P в " + rus_range;
console.log(result);

// Задача 2
temp = Number(prompt("Введите температуру"));
weather = prompt("Какая погода? (clear, cloudy, иное)");
let activity;
if (temp >= 25 && weather == "clear"){
    activity = "golf"
    console.log(activity)
}
else if (temp >= 10 && temp <= 24 || weather == "cloudy"){
    activity = "bowling"
    console.log(activity)
}
else {
    activity = "hiking"
    console.log(activity)
}

// Задача 3
a = Number(prompt("Введите первое число"));
b = Number(prompt("Введите второе число"));
sign = prompt("Выберите действие (+, -, *, /)");
if (sign == "+"){
    console.log(a + b)
}else if (sign == "-"){
    console.log(a - b)
}else if (sign == "*"){
    console.log(a * b)
}else if (sign == "/"){
    if (b == 0){
        console.log("Делить на 0 нельзя!")
    }
    console.log(a / b)
}else{
    console.log("Действие выбрано неправильно")
}

// Задача 4
let word = prompt("Введите слово");
let result;
let lenght = word.length;
let action = lenght ** 0.5;
if (action % 1 === 0) {
    result = 1
    console.log(result)
}
else {
    result = 0
    console.log(result)
}