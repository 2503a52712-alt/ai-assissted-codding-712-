# Python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


for celsius in [0, 25, 100]:
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.1f}°F")

    // JavaScript
function celsiusToFahrenheit(celsius) {
    return (celsius * 9 / 5) + 32;
}

for (const celsius of [0, 25, 100]) {
    const fahrenheit = celsiusToFahrenheit(celsius);
    console.log(`${celsius}°C = ${fahrenheit.toFixed(1)}°F`);
}