/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
 var decode = function(encoded, first) {
    /*
    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0
    */
    if (encoded.length === 0) {
        return [first]
    }
    var ans = []
    ans.length = encoded.length + 1
    ans[0] = first
    for (var i = 1; i < ans.length; i++) {
        ans[i] = ans[i - 1] ^ encoded[i - 1]
    }
    return ans
};