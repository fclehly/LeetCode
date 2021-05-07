/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
 var xorOperation = function(n, start) {
    var ans = 0
    for (var i = 0; i < n; i++) {
        ans = ans ^ (start + 2 * i)
    }
    return ans
};