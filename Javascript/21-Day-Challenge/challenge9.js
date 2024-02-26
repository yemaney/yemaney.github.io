/* Create a function that in an array representing a roster of astronauts.
Return an array containing the jobs of each astronaut.*/

const listAstronautJobs = (roster) => {
  // Code here!

  // initialize empty astronautJobs array to return
  let astronautJobs = [];

  // loop through length of roster
  for (let i = 0; i < roster.length; i++) {
    // check if astronaut has a job
    if (roster[i].hasOwnProperty('job')) {

      // add astronauts job to array
      astronautJobs.push(roster[i].job);
    }
  }
  return astronautJobs;
};


// using map

const listAstronautJobs = (roster) => {
  // Code here!

  return roster.map(astronaut => astronaut.job)
};
