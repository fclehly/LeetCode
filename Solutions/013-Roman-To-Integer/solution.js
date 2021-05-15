var romanToInt = function(s) {
    var roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    var ans = 0
    for (var i = 0; i < s.length; i++) {
        if (i + 1 < s.length && roman[s[i]] < roman[s[i + 1]]) {
            ans -= roman[s[i]]
        } else {
            ans += roman[s[i]]
        }
    }
    return ans
};

console.log(romanToInt("MCMXCIV"))