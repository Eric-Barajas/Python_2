/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
*/

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
abc: 42,
3: "wassup",
yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
const newObj = {}
// for loop goes here
for(let i = 0; i < keys.length; i++){
    // console.log(keys[i], values[i])
    newObj[keys[i]] = values[i]
}
Object.keys(newObj).map(key => {
    console.log(typeof(key))
})

}

console.log(zipArraysIntoMap(keys1, vals1))
console.log(zipArraysIntoMap(keys2, vals2))

//   const testObj = {}
// // {tyler: 'maxwell'}

// testObj['tyler'] = 'maxwell'

// console.log(testObj)