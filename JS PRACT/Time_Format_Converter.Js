function convertTo24Hour(time) {
    let [hour, minutePart] = time.split(":");
    let minute = minutePart.slice(0, 2);
    let period = minutePart.slice(2);

    if (period === "PM" && hour !== "12") {
        hour = parseInt(hour) + 12;
    }
    if (period === "AM" && hour === "12") {
        hour = "00";
    }

    return hour + ":" + minute;
}

console.log(convertTo24Hour("7:30PM"));
