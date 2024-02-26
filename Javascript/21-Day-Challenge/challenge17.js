/*
Your task is to write a function that will take in an array of toggle objects
 and a specific toggle name. The goal is to switch only the specific toggle, 
 without affecting the other toggles and then return the updated array.

Don't forget that you can use your previous function from the fourth challenge 
to help you complete it faster!
*/

const switchSpecificToggle = (toggleList, specificToggle) => {
    // Code here!
    toggleIdx = toggleList.findIndex(toggle => toggle.name === specificToggle);
    toggleList[toggleIdx].isOn = !toggleList[toggleIdx].isOn;
    return toggleList;
};



const toggleList = [
{
    name: "toggleA",
    isOn: false
    }, 
{
    name: "toggleB",
    isOn: true
}
]
const specificToggle = "toggleA"


console.log(toggleList);
console.log(specificToggle);
console.log(switchSpecificToggle(toggleList, specificToggle));
