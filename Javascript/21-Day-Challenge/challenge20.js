/*
Your task is to write a function that will take in speed (number), missionData (object) 
and checks (object) as parameters. The goal is to make sure that the speed is within the 
limits and that the amount of entries per type matches with the checks. If one of the values 
is a mismatch, return false, if everything is fine, return true.

Speed will be compared against maxSpeed and minSpeed inclusively and the length of each 
array inside missionData will be compared to the values inside the dataEntries object values.
*/

const checkSpeedLimit = (speed, { minSpeed, maxSpeed }) => {
    // Check if speed is between minSpeed and maxSpeed inclusively
    return (minSpeed <= speed && speed <= maxSpeed); 
};


const checkMissionCounts = (missionData, { dataEntries }) => {
    // check equality of missionData arrays with their respective dataEntries object values
    // return true if all checks are true, else false
    return Object.keys(missionData).reduce((acc, key) => {
        acc *= missionData[key].length == dataEntries[key];
        return Boolean(acc);
    }, true);
};


const confirmReentryPlans1 = (speed, missionData, checks) => {
    // Code here!
    // Using functions
    return checkSpeedLimit(speed, checks) && checkMissionCounts(missionData, checks);
};


const confirmReentryPlans2 = (speed, missionData, checks) => {
    // Code here!
    // using loops
    if (speed < checks.minSpeed || speed > checks.maxSpeed) {
        return false;
    }
    
    for (let x in missionData) {
        if (missionData[x].length != checks.dataEntries[x]) {
            return false;
        }
    }

    return true;
};


const speed = 40
const missionData = {
    astro: ["...", "..."],
    bio: ["..."],
    physics: ["..."]
}

const checks = {
    maxSpeed: 50,
    minSpeed: 20,
    dataEntries: {
        astro: 3,
        bio: 1,
        physics: 1
    }
}


console.log(speed);
console.log(missionData);
console.log(checks);
console.log(confirmReentryPlans1(speed, missionData, checks));
console.log(confirmReentryPlans2(speed, missionData, checks));