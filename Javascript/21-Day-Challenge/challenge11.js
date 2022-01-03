/* Create a function that takes platformList a list of objects with bookDate a property
and a missionDate string. Update the first object with an empty bookDate with the missionDate  */

const bookFreePlatform1 = (platformList, missionDate) => {
    // Code here!
    // Using loop through the list of platforms
    for (let i = 0; i < platformList.length; i++) {
        // check condition, and return on the first match
        if (platformList[i].bookDate === undefined) {
            platformList[i].bookDate = missionDate;
            return platformList;
        }
    }
};


const bookDateIsUndefined = (element) => element.bookDate == undefined;

const bookFreePlatform = (platformList, missionDate) => {
    // Code here!
    // Using findIndex method
    let i = platformList.findIndex(bookDateIsUndefined);
    platformList[i].bookDate = missionDate;
    return platformList;
};

const missionDate = "2021-12-12"
const platformList = [
    {
        name: "Platform A",
        bookDate: "2021-12-11"
    },
    {
        name: "Platform B",
        bookDate: undefined
    },
    {
        name: "Platform C",
        bookDate: undefined
    },
];

console.log(platformList);
console.log(bookFreePlatform(platformList, missionDate));
