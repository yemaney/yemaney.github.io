/*
Your last (!) task is to write a function that will take in an array of exchanged messages and an array 
of organized data. The goal is to parse each message, add them to a list and return an object containing 
two keys, transcript with the messages, missionData with the missionData object.

Each message should be parsed using the same structure as the first challenge;
*/


const parseMissionSummary = (exchanges, missionData) => {
    // Code here!
    let transcript = exchanges.map(({ origin, message }) => (origin + ': ' + message));
    return { transcript, missionData };
};


const exchanges = [
    { origin: "MC", message: "So how is it out there?" },
    { origin: "Shuttle", message: "Oh it's pretty nice!" },
    { origin: "MC", message: "Did you like the challenges?" },
]

const missionData = {
    astro: ["...", "..."],
    bio: ["..."],
    physics: ["..."]
}

console.log(exchanges);
console.log(missionData);
console.log(parseMissionSummary(exchanges, missionData));