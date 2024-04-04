const cheerio = require("cheerio");
const axios = require("axios"); // loading in all the packaghes

function getPostings() {
  console.log("Entered getPostings");
  const url = "https://sandiego.craigslist.org/search/zip#search=1~gallery~0~0";
  const max = 40;
  let counter = 0;

  return axios.get(url).then((response) => {
    console.log("Entered axios.get.then()");
    const postings = [];
    console.log("Inital Posting Values:");
    //console.log(postings);

    const $ = cheerio.load(response.data);

    $("li.cl-static-search-result").each((i, element) => {
      if (postings.length < max) {
        counter++;
        //console.log("Found Posting: " + counter);
        const title = $(element)
          .attr("title")
          .replace(/[\n\s]/g, "_");
        const link = $(element).find("a").attr("href");
        const location = $(element)
          .find(".location")
          .text()
          .replace(/[\n\s]/g, "");
        let postingObject = {
          title,
          location,
        };
        //console.log("info");
        //console.log(postingObject);
        postings.push(postingObject);
      }
    });
    console.log("Final Posting Values before returning");
    //console.log(postings);
    return postings;
  });
  //return "filler text";
}

module.exports = { getPostings };
