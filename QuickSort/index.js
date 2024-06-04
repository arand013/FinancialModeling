
// The quicksort function takes an array as input and returns a sorted array
function quicksort(anArray) {

// If the array has one or zero elements, it is already sorted, so we return it as is
    if (anArray.length <= 1) {
        return anArray;
    }

// Choose the first element as the pivot
    let pivot = anArray[0];

 // Create two new arrays: less for elements less than the pivot, and greater for elements greater than the pivot
    let less = [];
    let greater = [];

 // Iterate through the array starting from the second element (index 1)
    for (let i = 1; i < anArray.length; i++) {

// If the current element is less than the pivot, add it to the less array

        if (anArray[i] <= pivot) {
            less.push(anArray[i]);
        } else {

// If the current element is greater than the pivot, add it to the greater array
            greater.push(anArray[i]);
        }
    }

// Recursively call the quicksort function on the less array and the greater array
    return [...quicksort(less), pivot, ...quicksort(greater)];
}

// Test the function with an example array
let array = [5, 2, 8, 3, 1, 6, 4];
console.log(quicksort(array));