/*
Your task is to write a function that will take in a list of data entries
in the shape of an array of objects. The function will then organize and
return the entries by type and store each bit of data (string) in each 
list, in the shape of an object containing arrays.
*/

const organizeData = (receivedData = []) => {
    // Code here!

    return receivedData.reduce((acc, item) => {
        acc[item.type] = (acc[item.type] || []);
        acc[item.type].push(item.data);
        return acc
    }, {});

};



const listOfReceivedData = [
    { type: "astro", data: "Saturn Data" },
    { type: "bio", data: "Space Potatoes" },
    { type: "physics", data: "Lagrange Points" },
    { type: "bio", data: "OMG Tardigrades" },
    { type: "physics", data: "Material reflectivity" },
    { type: "astro", data: "Mercury is not the hottest" },
];

console.log(listOfReceivedData);
console.log(organizeData(listOfReceivedData));
